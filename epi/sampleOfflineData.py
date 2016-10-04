
# given an array, and a size k
# return a random sample of size k, return it whithin the array

# approach is, as random values are picked, move them to the front
# until k values have been obtained
# you end up with, randomn values of size k | other elements

import random

def sampleOfflineData(values, k):

    # move k values to the front as they are found
    size = len(values)-1

    for i in range(k):
        
        index = random.randint(i, size)
        print 'swapping {} and {}'.format(i, index)
        values[i], values[index] = values[index], values[i]
        print values

    print 'new values after sample 4 of them', values
    print 'focusing on the first 4', values[:k]


a = [4, 1, 2, 7, 5, 9]

print 'original values, looking to get a sample of size 4', a
sampleOfflineData(a, 4)



