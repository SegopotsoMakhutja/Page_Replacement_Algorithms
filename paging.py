import sys
import numpy
import random

# Author: Segopotso Makhutja
# MKHSEG001
# paging.py - a python program that implements
# FIFO, LRU, and optimal
# page replacement algorithms

# <----------------------------START README---------------------------->

# this section is just an explanation of my program and assumptions made.
# the program runs as the assignment brief asks
# it should be noted that I 
# generate a page refStr length between 0-60 (but can handle any length) 
# and the numbers range from 0-9
# since the assignment brief was not very clear on this
# the size is user determined when the program is run
# the program should be run as follows on the command line:
# python paging.py <number of page frames>
# number of page frames ranges between 1-7

# <-----------------------------END README----------------------------->

# the fifo algorithm
def FIFO(size, pages):
    nframes = size
    pages = pages
    npfaults, head, flag = 0, 0, 0
    memory = []
    
    for i in pages:
        if i not in memory:
            if len(memory) < nframes:
                memory.append(i)
            else:
                memory[head] = i
                head = (head+1) % nframes
            npfaults += 1
            flag = 1
        else:
            flag = 0
    print("\nTotal pages:", len(pages), end='\n') 
    
    return npfaults

# least recently used
def LRU(size, pages):
    nframes = size
    pages = pages
    npfaults, flag = 0, 0
    memory, swp = [], []
    
    for i in pages:
        if i not in memory:
            if len(memory)<nframes:
                memory.append(i)
                swp.append(len(memory)-1)
            else:
                head = swp.pop(0)
                memory[head] = i
                swp.append(head)
            npfaults += 1
            flag = 1
        else:
            swp.append(swp.pop(swp.index(memory.index(i))))
            flag = 0

    print("\nTotal pages:", len(pages), end='\n') 
    
    return npfaults

# optimal algorithm for page replacement
def OPT(size, pages):
    nframes = size
    pages = pages
    npfaults, flag = 0, 0
    memory = []

    occur = [None for i in range(nframes)]
    for i in range(len(pages)):
        if pages[i] in memory:
            flag = 0
        else:
            flag = 1
            if len(memory) < nframes:
                memory.append(pages[i])
            else:
                for x in range(len(memory)):
                    if memory[x] in pages[i+1:]:
                        occur[x] = pages[i+1:].index(memory[x])
                    else:
                        memory[x] = pages[i]
                        break
                else:
                    memory[occur.index(max(occur))] = pages[i]
            npfaults += 1

    print("\nTotal pages:", len(pages), end='\n') 
    
    return npfaults

# main method, entry into the program
def main():
    #testrefStr = [8,5,6,2,5,3,5,4,2,3,5,3,2,6,2,5,6,8,5,6,2,3,4,2,1,3,7,5,4,3,1,5]
    # a list of randomly generated numbers ranging from 0-9
    refStr = []
    # generates a runmber file refStr length between 0-60
    for x in range(random.randint(0, 61)):   
        refStr.append(random.randint(0, 9))
    # print("the reference string: ", refStr, end="")
    pages = refStr
    #pages = testrefStr
    size = int(sys.argv[1])
    #size = random.randint(1, 7)
    print('FIFO', FIFO(size, pages), 'page faults.', end='\n')
    print('LRU', LRU(size, pages), 'page faults.', end='\n')
    print('OPT', OPT(size, pages), 'page faults.', end='\n')

if __name__ == "__main__":
    #main()
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of pages]')
    else:
        main()