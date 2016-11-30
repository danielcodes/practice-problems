
# multiply two integers given in array form
# n*m can be at most length of n + m
# perform operation by multiplying each digit in second num 
# with the first num
# [-1, 1] x [1, 2] = [-1, 3, 2]

def multiplyInts(a, b):

    # gotta take care of sign
    # assumes non empty array inputs..
    sign = 1
    if a[0] < 0 and b[0] < 0:
        sign = 1
    elif a[0] < 0 or b[0] < 0:
        sign = -1

    a[0] = abs(a[0])
    b[0] = abs(b[0])

    result = [0]*(len(a) + len(b))

    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):

            # first multiplies everything into one slop
            # if there is a carry, put it in the left slot next to it
            # retain only the rightmost value in the original slot
            result[i+j+1] += a[i] * b[j]
            result[i+j] += result[i+j+1] / 10
            result[i+j+1] %= 10

    # handle sign, ugliness
    k = 0
    while result[k] == 0:
        # move until you get to first nonzero value
        k += 1
    result[k] *= sign

    return result


a = [1, 2, 3]
b = [9, 8, 7]

print 'Multiplying {} with {} gives {}'.format(a, b, multiplyInts(a, b))

a = [-1, 1]
b = [1, 2]

print 'Multiplying {} with {} gives {}'.format(a, b, multiplyInts(a, b))



