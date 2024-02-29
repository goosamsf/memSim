import util

'''
- Write function for reading address.txt file and get each element : this is our main
- Write function that can extract page number and page offset from logical address
- Write function that handle page fault
'''
ptable = [-1] * 256
ph_mem = [-1] * 256
tlb = {}
tlbcount = 0
ptablecount = 0
faultcount = 0

#Read address.txt
with open('addresses.txt', 'r') as file:
    for addr in file:
        page = util.extract_page(int(addr))
        pnum = page[0]
        poff = page[1]
        if pnum in tlb:
            tlbcount+=1
            continue
        elif ptable[pnum] != -1:
            ptablecount+=1
            continue
        else: 
            faultcount +=1
            util.pfault_handler(int(addr), pnum, poff, ptable, ph_mem, tlb)



    
