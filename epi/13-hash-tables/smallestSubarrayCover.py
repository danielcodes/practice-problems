
# given an array of words and a set of words
# find the smallest subarray that contains all the words in the set
# approach, move right until we have a subarray that contains all words in the set
# the move left until it is lost and look right again, do this till the end

def smallestSubarray(paragraph, words):

    print 'the paragraph is', paragraph
    print 'the set of words is', words

    # build up dict first
    wordCounter = {}
    for w in words:
        if w in wordCounter:
            wordCounter[w] += 1
        else:
            wordCounter[w] = 1

    words_remaining = len(wordCounter)

    left = 0
    right = 0
    result = (-1, -1)

    # move right until we hit a solution
    while right < len(paragraph):

        # if we see a word from the set
        # decrement count from dict and counter
        if paragraph[right] in wordCounter:
            wordCounter[paragraph[right]] -= 1
            words_remaining -= 1

        # at this point, we have a solution
        # shift left until we lose it
        # works even for edge cases when there is only one element at the end
        # left is set out of bounds but never accessed as when right goes out of bounds
        # that terminates the loop
        while words_remaining == 0:

            # update result
            if result == (-1, -1) or (right - left) < (result[1] - result[0]):
                result = (left, right)
            
            # check if word is a keyword
            # if so, increase count on dict and counter
            if paragraph[left] in wordCounter:
                wordCounter[paragraph[left]] += 1
                words_remaining += 1

            left += 1
        right += 1

    return result

paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 
             'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
words = ['banana', 'cat']

result = smallestSubarray(paragraph, words)
print 'the smallest subarray containg the set of words is', result


