
# printing a 2D array in a spiral manner
# main idea is to use 4 variables to keep track of what to print
# these limiters shrink the array until nothing is left to print

a = [[2, 4, 6, 8],
     [5, 9, 12, 16],
     [2, 11, 5, 9],
     [3, 2, 1, 8]]


def printSpiral(arr):

    # 4 limiters, top, bot, left and right
    t = 0
    b = len(arr)-1
    l = 0
    r = len(arr[0])-1

    # direction to be updated on each iteration
    d = 0

    # 0 right, 1 down, 2 left, 3 up
    while t <= b and l <= r:
        print 'start'
        # print t, b, l, r
        if d == 0:
            for i in range(l, r+1):
                print arr[t][i]
            t += 1
        elif d == 1:
            for j in range(t, b+1):
                print arr[j][r]
            r -= 1
        elif d == 2:
            for k in range(r, l-1, -1):
                print arr[b][k]
            b -= 1
        else:
            for h in range(b, t-1, -1):
                print arr[h][l]
            l += 1
        d = (d+1) % 4

        print 'finish'
for i in a:
    print i
printSpiral(a)





