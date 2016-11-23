
# find whether the string can be made with words from a set
# approach, keep an list of the lengths of the last word that this index holds
# a prefix is valid, if it is a word or if a smaller prefix is valid and the rest is a word
# to give back the words, start from the end and build up the words

def decomposeIntoWords(string, words):
    
    # create length array first
    l = len(string)
    lastLength = [-1] * l
    for idx in range(l):

        # we have a word
        if string[:idx+1] in words:
            lastLength[idx] = idx+1

        # step through j < i, and see if it can be split
        if lastLength[idx] == -1:
            i = 0
            found = 0
            while i < idx and not found:
                # a subprefix must be valid and the remainder is a word
                # print 'the split is', string[:i+1], string[i+1:idx+1]

                # super rusty with this slice notation
                # if you do s[1:1], results in '', gotta go one above
                if (lastLength[i] != -1) and (string[i+1:idx+1] in words):
                    # print 'found a split, saving', string[:i+1], string[i+1:idx+1]
                    lastLength[idx] = idx-i
                    found = 1
                i += 1

    words = []
    if lastLength[-1] != -1:
        # get the words in a backwards manner
        cur = l-1
        while cur >= 0:
            words.append(string[cur-lastLength[cur]+1:cur+1])
            cur = cur - lastLength[cur]

        words.reverse()
        return words
    
    return words


if __name__== '__main__':

    words = set(['a', 'man', 'plan', 'canal'])
    string = 'amanaplanacanal'

    print 'Can we make "{}" from the words given in {}?'.format(string, words)
    print 'the words are', decomposeIntoWords(string, words)

    print '-------------------------------------------------------'

    words = set(['a', 'man', 'jest', 'canal'])
    string = 'amanaplanacanal'

    print 'Can we make "{}" from the words given in {}?'.format(string, words)
    print 'the words are', decomposeIntoWords(string, words)


