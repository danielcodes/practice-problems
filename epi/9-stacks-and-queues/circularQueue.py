
# implement a circular queue API
# constructor takes an initial capacity
# enqueue and dequeue functions, an additional size function
# dynamic resizing when out of space

# ie [2, 3, 4, 1], [1, 2, 3, 4, 5]
#           t  h    h           t
# -> [1, 2, 3, 4, ...], where ... is the additional space added

# too damn hacky

class CircularQueue:

    # begin, begin+head, end
    def __init__(self, capacity):

        self.head = 0
        self.tail = 0
        self.numOfElements = 0
        self.values = [0] * capacity

    
    def enqueue(self, num):

        # when queue is full
        if self.numOfElements == len(self.values):
            # imitating rotation, a left shift
            # rotate 'head' times
            self.values = self.values[self.head:] + self.values[0:self.head]
            self.head = 0
            self.tail = self.numOfElements

            # can't do the resize, so just gonna append a list
            self.values = self.values + [0]*len(self.values) 

        self.values[self.tail] = num
        self.tail = (self.tail + 1) % len(self.values)
        self.numOfElements += 1

        print 'adding', self.values, 'added', num


    def dequeue(self): 
        
        if len(self.values) == 0:
            raise Exception('Queue is empty!')

        self.numOfElements -= 1
        item = self.values[self.head]
        self.head = (self.head+1) % len(self.values)

        print 'deleting', self.values, 'new head at index,', self.head
        return item

    
    def size(self):
        return self.numOfElements


q = CircularQueue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print 'current number of elements is', q.size()

q.dequeue()
q.dequeue()

print 'current number of elements is', q.size()

q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

print 'current number of elements is', q.size()


