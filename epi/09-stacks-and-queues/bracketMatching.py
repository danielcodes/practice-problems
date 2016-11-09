
# test whether a string contain a set of brackets is well-formed
# every opening bracket has a closer
# approach, use a stack

def bracketsMatch(exp):

    s = []
    for c in exp:
        
        if c == '(' or c == '[' or c == '{':
            s.append(c)
        else:
            # stack is empty, error
            if len(s) == 0:
                raise Exception('stack is empty!')

            # a closer
            opener = s.pop()
            if opener == '(' and c != ')':
                return False
            elif opener == '[' and c != ']':
                return False
            elif opener == '{' and c != '}':
                return False

    return len(s) == 0


a = '{()[]}'
print 'is the expression {}, well formed? {}'.format(a, bracketsMatch(a))
b = '[(])'
print 'is the expression {}, well formed? {}'.format(b, bracketsMatch(b))


