
# closesst pair of repeated words in a sentence
# approach is to use a hash table to look up prev idx of the words
# if it exists compare it to current min, otherwise add it in

def closestPair(words):
    
    # returning distance
    # gotta set this to the highest value first
    indexes = {}
    closestDist = float('infinity')
    
    for index, word in enumerate(words):
        
        prevIdx = indexes.get(word)
        if prevIdx != None:
            # print 'currently looking at, {} at index, {}'.format(word, index)
            closestDist = min(closestDist, index - prevIdx)
        
        indexes[word] = index
    
    return closestDist
    

a = 'All work and no play makes for no work no fun and no results'
print 'the sentence is,', a
a = a.split(' ')
res = closestPair(a)
print 'the closest distance between two repeated words is,', res

