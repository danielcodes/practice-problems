
# there are cities arranged in a circular road
# at each city, you refill gas and to get to the next one you need to travel x miles
# an ample city is a city for which you start and complete the road and do not
# run out of gas at any point

# approach is to see the relationship between dist vs. gas
# we want the city that start with the minimum amount of gas
# if we start at this city, as we traverse the road, it will never dip below this minimum

# O(n) time, one pass
# O(1) space, no additional storage

def gasupProblem(gas, miles):

    # miles per gallon
    MPG = 20

    remaining = 0
    result = {'city': 0, 'gasRemaining': 0}

    for i in range(1, len(gas)):

        remaining += gas[i-1] - miles[i-1] / MPG
        # found a new min
        if remaining < result['gasRemaining']:
            result['city'] = i
            result['gasRemaining'] = remaining
    
    # print result
    return result['city']

gas = [50, 20, 5, 30, 25, 10, 10]
miles = [900, 600, 200, 400, 600, 200, 100]

print 'gas refills at each city,', gas
print 'miles needed to travel are,', miles
print 'the ample city is at index,', gasupProblem(gas, miles)


