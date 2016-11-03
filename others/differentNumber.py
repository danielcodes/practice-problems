
# given an array of n numbers, find a value not in the array
# approach, use pigeon hole principle
# for an array of size 4, can hold only up to its n-1 index
# so we build a n+1 size array, fill it and look for the missing value

def differentNumber(numbers):

    n = len(numbers)+1
    buckets = [0] * n

    # filling up the buckets
    for num in numbers:
        buckets[num%n] = 1

    for i in range(n):
        # found a missing number
        if buckets[i] == 0:
            return i


numbers = [1, 5, 9, 10]
result = differentNumber(numbers)

print numbers
print 'a missing number in this list is', result


