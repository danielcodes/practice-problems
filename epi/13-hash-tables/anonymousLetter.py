
# making a letter out of a magazine
# the approach is to create a hash table that contains <char, freq> for each char
# then pass through the magazine and decrement count
# if it hits 0, pop it
# at the end if the hash is empty, T, else F

def letterFromMagazine(letter, magazine):

    print 'letter is -', letter, len(letter)
    print 'magazine is -', magazine

    # start with creating the hash for the letter
    letterChars = {}
    for char in letter:
        
        # if +1, else init it to 0
        if char in letterChars:
            letterChars[char] += 1
        else:
            letterChars[char] = 1
            
    print 'characters in the letter', letterChars

    # now walk through the magazine and decrement
    for c in magazine:

        if c in letterChars:
            letterChars[c] -= 1

            if letterChars[c] == 0:
                letterChars.pop(c)

    print 'characters that the magazine cannot provide', letterChars

    if not letterChars:
        print 'can make the letter'
        return True
    else:
        print 'cannot make the letter'
        return False


letter = 'hello, how are you?'
magazine = 'xyz hello, how are you'

letterFromMagazine(letter, magazine)


