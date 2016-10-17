
# given a set of words separated by spaces
# reverse the words, this solution assumes clean input

# approach, find the next space and reverse word from start to end

def reverseChars(string, start, end):

    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    

def reverseWords(words):

    chars = list(words)
    length = len(chars)

    # reverse all the words first
    reverseChars(chars, 0, len(chars)-1)

    start = 0
    end = 0

    # iterate one by one
    while end < length:

        # reverse when it hits a space
        if chars[end] == ' ':
            reverseChars(chars, start, end-1)
            start = end + 1
        elif end == length-1:
            # reached the last word, reverse it
            reverseChars(chars, start, end)
        end += 1
        
    return ''.join(chars)

# strings are immutable so use list of chars
words = 'studious is Daniel'
print words
print 'after reversing the words,', reverseWords(words)


