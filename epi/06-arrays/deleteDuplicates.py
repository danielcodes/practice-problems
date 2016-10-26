
# delete duplicate items from a sorted array
# approach, step through and compare current idx with prev value
# if equal, go to next, if not, write to the next available slot

# O(n) time, one pass
# O(1) space

def deleteDuplicates(values):

    write_idx = 1
    length = len(values)

    for i in range(1, length):

        # write only when prev is not the same
        if values[i] != values[i-1]:
            values[write_idx] = values[i]
            write_idx += 1

    return values


l = [2, 3, 5, 5, 7, 11, 11, 11, 13]
result = deleteDuplicates(l)
print 'before', l
print 'after', result


