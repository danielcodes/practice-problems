
# implement a queue using two stacks
# use one stack to push items in
# to dequeue, move items from s1 to s2 and pop from there

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []


    def enqueue(self, value):
        print 'adding', value, 'to s1', self.s1, self.s2
        self.s1.append(value)


    def dequeue(self):

        # second stack not empty
        if self.s2:
            print 'popping from s2', self.s1, self.s2

            return self.s2.pop()

        # move from s1 to s2
        if len(self.s1) == 0:
            raise Exception('Queue is empty!')
        else:
            while self.s1:
                self.s2.append(self.s1.pop())

        print 'moved from s1 to s2 and then popping', self.s1, self.s2
        return self.s2.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.dequeue()
q.enqueue(1)
q.dequeue()


