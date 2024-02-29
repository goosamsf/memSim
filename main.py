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

    
ptable = [-1] * 256
ph_mem = [-1] * FRAMES
tlb = {}
tlbcount = 0
ptablecount = 0
faultcount = 0

#Read address.txt
with open(FILENAME, 'r') as file:
    for addr in file:
        page = util.extract_page(int(addr))
        pnum = page[0]
        poff = page[1]
        if pnum in tlb:
            print("tlb hit")
            tlbcount+=1
            continue
        elif ptable[pnum] != -1:
            print(pnum)
            print("ptable hit")
            print(ptable)
            ptablecount+=1
            continue
        else: 
            faultcount +=1
            util.pfault_handler(int(addr), pnum, poff, ptable, ph_mem, tlb, PRA)
        
        


    
