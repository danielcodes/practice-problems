
# towers of hanoi problem
# given 3 pillars
# first one has a pyramid like structure, ie 1, 2, 3, 4
# second and third are empty
# goal is to move this structure to the middle, moving only one disk at a time
# and a larger disk cannot be on top of a smaller one

def towerOfHanoiStep(disks, pillars, from_, to_, use_):
	
    '''the idea behind it 
      #	     #    #
     ###     #    #
    #####    #    #  
    
    1st, move everything but the last to the 3rd pillar
    2nd, move the last disk to the 2nd pillar
    3rd, move the disks in the 3rd pillar to the second
    '''
    
    # recursive step 
    if disks > 0:
        # recurse down until there is one disk left
        towerOfHanoiStep(disks-1, pillars, from_, use_, to_)
        pillars[to_].append( pillars[from_].pop() )
        print 'moving from', from_, 'to', to_
        towerOfHanoiStep(disks-1, pillars, use_, to_, from_)	


# execute
pillars = []

# change # of disks 
diskNum = 3

for i in range(1, diskNum+1):
    pillars.append([])
    pillars[0].append(i)
	
print pillars

towerOfHanoiStep(diskNum, pillars, 0, 1, 2)

print pillars


