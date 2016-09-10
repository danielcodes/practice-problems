
# check whether the parenthesis of aan expression is balanced

def is_balanced(exp):

    brackets = { '(': ')', '[': ']', '{': '}' }
    s = []

    for c in exp:
            
        if c in brackets.keys():
            s.append(c)
        else:
            # is a closer
            opener = s.pop()
            if brackets[opener] != c:
                return False
                
    return True

expression = '[(])'

print 'checking that the expression {} is balanced, {}'.format(expression, is_balanced(expression))




