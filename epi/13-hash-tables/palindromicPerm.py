
# find if a permutation of a string is a palindrome
# approach, keep a hashmap with char keys and their counts
# iterate through the counts and if there is more than one odd, no palindrome

def palindromicPerm(string):

    chars = {}
    for c in string:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    # print chars
    # second pass
    oddCount = 0
    for ch in chars:

        if chars[ch] % 2 == 1:
            oddCount += 1

            # ugly nested if
            if oddCount > 1:
                return False

    return True


s = 'edified'
print "cand the word '{}' be turned into a palindrome? {}".format(s, palindromicPerm(s))

a = 'civil'
print "cand the word '{}' be turned into a palindrome? {}".format(a, palindromicPerm(a))


