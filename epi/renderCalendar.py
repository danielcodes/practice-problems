
# given a set of intervals, find the maximum number of events that are happening concurrently
# brute force is to check each interval against each other for overlap, results in O(n^2)
# a better approach is to first sort and focus on endpoints, step through them
# if its a start, add it to a counter otherwise decrement

from operator import itemgetter

def findConcurrentEvents(events):
    
    # first convert to endpoints, (time, isStart)
    endpoints = []
    for e in events:
        # push both values in, one start, one end
        endpoints.append((e[0], 1))
        endpoints.append((e[1], 0))

    # move all starts to the front first
    # then sort based on time, if times are the same, order is preserved
    # from the previous sort, all starts are in the front
    endpoints.sort(key=itemgetter(1), reverse=True)
    endpoints.sort(key=itemgetter(0))

    numOfEvents = 0
    maxEvents = 0

    for end in endpoints:
        # a start
        if end[1] == 1:
            numOfEvents += 1
            maxEvents = max(numOfEvents, maxEvents)
        else:
            numOfEvents -= 1

    return maxEvents


# represent as a list of tuples
events = [(4, 5), (9, 17), (2, 7), (8, 9), (12, 15), (1, 5), (6, 10), (12, 13), (14, 15)]

print 'the events are', events
print 'the maximum number of concurrent events is', findConcurrentEvents(events)


