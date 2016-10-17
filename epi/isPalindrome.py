
# testing whether a string is a palindrome
# a string that is spells the same forward and backwards
# ignore non-alphanumeric values and turn everything lowercase

# approach is to use two indexes

def isPalindrome(string):

    start = 0
    end = len(string)-1

    while start < end:

        # move front and bock until we land at an alnum char
        while not string[start].isalnum() and start < end:
            start += 1

        while not string[end].isalnum() and start < end:
            end -= 1

        # print 'currently comparing', string[start], string[end]

        if string[start].lower() != string[end].lower():
            return False
        
        start += 1
        end -= 1

    return True


strings = ['A man, a plan, a canal, Panama', 'Able was i, ere I saw Elba!', 'Ray a Ray']

print 'testing for palindromes'
for s in strings:
    print s
    print 'is the string a palindrome?', isPalindrome(s), '\n'


