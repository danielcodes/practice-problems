
# check if an integer is a palindrome
# same check that is applied to strings
# trick is getting the first digit in the number

import math

def isIntPalindrome(n):

    if n<0:
        return False
    elif n == 0:
        return True

    # find the # of digits
    d = int(round(math.log(n, 10))) + 1

    # grabbing the MSD and LSD
    msd_mask = int(math.pow(10, d-1))

    for i in range(len(str(n))/2):

        # check endpoints
        if n/msd_mask != n%10:
            return False

        # take off far left and far right digits
        # and update mask
        n %= msd_mask
        n /= 10

        msd_mask /= 100

    return True


n = 157151
print 'is the integer {} a palindrome? {}'.format(n, isIntPalindrome(n))

n = 157751
print 'is the integer {} a palindrome? {}'.format(n, isIntPalindrome(n))


