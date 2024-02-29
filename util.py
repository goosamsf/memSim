
TLB_SIZE = 16
PAGE_SIZE = 256
LOGICAL_ADDRESS = 0xFFFF
PAGE_NUMBER_OFFSET = 8
PAGE_OFFSET_OFFSET = 0xFF

victim_frame = 0

def extract_page(logical_addr): 
    #Extract Page elements. Page consiste of page number and page offset
    #We want to look at 32bit integer of logical address,
    #First take the low 16bits and from their high 8bit is page number and low 8bit is page offset
    addr = logical_addr & LOGICAL_ADDRESS 
    pn = addr >> PAGE_NUMBER_OFFSET
    po = addr & PAGE_OFFSET_OFFSET 

    return (pn,po) 

def pfault_handler(addr, pnum,poff, ptable, ph_mem, tlb, pra):
    # When both tlb and page table wasn't able to retrieve corresponding value,
    # this is called and do following:
    # 1. Find available spot in physical memory.
    # 2. Read 256 bytes from 256*page_number th bytes using seek function
    # 3. combine frame number with page_offset.
    # 4. Update tlb and page table so that subsequent access can make use of it 
    
    #replaceflag is initially set to true, then iterate over physical memory.
    #if free space is found, set it false so that PRA is not invoked. 
    replaceflag = 1 
    frame_num = -1
    for i in range(len(ph_mem)):
        if ph_mem[i] == -1:
            frame_num = i
            replaceflag = 0
            break
    
    f = open('BACKING_STORE.bin', 'rb')
    f.seek(int(pnum)* PAGE_SIZE)
    
    # readbytes's type is byte array , we want to show this in hexadecimal form
    readbytes = f.read(PAGE_SIZE) 
    readb = ''.join(format(byte, '02x') for byte in readbytes)
    
    # value is the byte stored in memory at the address(in Backing_STORE.bin) 
    # First go to the proper position using page offset and extract the byte 
    # next, convert it using int.from_bytes, signed flag is required for outputting standard.
    value = readbytes[poff:poff+1] 
    value = int.from_bytes(value,"big", signed="True")

    f.close()

    # Combine frame number with page offset
    fn = frame_num << 8 
    fn = fn | poff
    
    # Update tlb and page table
    if replaceflag and pra == "fifo" :
        #fifo
        global victim_frame
        frame_num = victim_frame
        fifo_handler(fn, pnum, ptable, ph_mem, tlb)
        
    else:
        ph_mem[frame_num] = fn
        ptable[pnum] = frame_num 
        if len(tlb) > TLB_SIZE :
            first_key = next(iter(tlb))
            tlb.pop(first_key)
        tlb[pnum] = frame_num 

    frame_vs_page(frame_num ,pnum) 
    #print("{}, {}, {}, {}".format(addr, value, frame_num, readb.upper()))


def frame_vs_page(frame_num , page_num):
    print(str(frame_num) + " : " + str(page_num))

def fifo_handler(fn,pnum, ptable, ph_mem, tlb):
    #when pra is set to "fifo" , this function is invoked.
    #What this does is very simple. We have global variable
    #victim_frame initially set to 0. So
    # 0. Delete previous element from ptable tlb so that no two elements point 
    #    same physical address 
    # 1. Replace physical memory's victim_frame index with new frame
    # 2. update page table and tlb
    # 3. Increment victim_frame but if incremented victim_frame is FRAMES
    #    set it to 0
    global victim_frame
    ph_mem[victim_frame] = fn

    for i in range(len(ptable)):
        if ptable[i] == victim_frame:
            ptable[i] = -1
            break

    ptable[pnum] = victim_frame
    for key in tlb:
        if tlb[key] == victim_frame:
           tlb.pop(key) 
           break

    if len(tlb) > TLB_SIZE:
        first_key = next(iter(tlb))
        tlb.pop(first_key)
    tlb[pnum] = victim_frame
    victim_frame+=1
    if victim_frame == len(ph_mem):
        victim_frame = 0
    
    return


