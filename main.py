import util
import sys

'''
- Write function for reading address.txt file and get each element : this is our main
- Write function that can extract page number and page offset from logical address
- Write function that handle page fault
'''
if len(sys.argv) < 2:
    print("usage: memSim <reference-sequence-file.txt> <FRAMES> <PRA>")
    sys.exit()

#Default Constants
lruflag = 0
FRAMES = 256
PRA = "fifo"
FILENAME = sys.argv[1]
if len(sys.argv) == 3:
    #PRA is omitted
    FRAMES = int(sys.argv[2])
elif len(sys.argv) == 4:
    #NO ARGS are omitted
    FRAMES = int(sys.argv[2])
    PRA = sys.argv[3]
    if PRA == "lru":
        lruflag = 1

    
ptable = [-1] * 256
ph_mem = [-1] * FRAMES
lru_container = []
tlb = {}
tlbcount = 0
ptablecount = 0
faultcount = 0
num = 0
#Read address.txt
with open(FILENAME, 'r') as file:
    for addr in file:
        num+=1
        page = util.extract_page(int(addr))
        pnum = page[0]
        poff = page[1]
        if pnum in tlb:
            print("tlb hit")
            #print(ptable[pnum])
            #print(lru_container)
            tlbcount+=1

            util.lru_modify(1, ptable[pnum],lru_container,0)
            continue
        elif ptable[pnum] != -1:
            print("ptable hit")
            print(tlb)
            util.tlb_update(pnum, ptable, tlb)
            print(tlb)
            ptablecount+=1
            continue
        else: 
            faultcount +=1
            util.pfault_handler(int(addr), pnum, poff, ptable, ph_mem, tlb, PRA, lru_container)

print("Number of Translated Addresses = " + str(num))
print("Page Faults = " + str(faultcount))
print("Page Fault Rate = {:.3f}".format(num/faultcount))
print("TLB Hits = " + str(tlbcount))
print("TLB Misses = " + str(num-tlbcount))
print("TLB Hit Rate = {:.3f}".format((tlbcount/num)))
        
        


    
