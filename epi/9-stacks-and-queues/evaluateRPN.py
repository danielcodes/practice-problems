
# evaluate an expression in reverse polish notation
# ie. 3, 4, +, 2, x, 1, +
# translates to (3+4) x 2 + 1

# approach, use a stack, push values in
# compute if an operator is seen and push back to stack

def evaluateRPN(exp):
    
    # assumes a vaild RPN exp
    exp = exp.split(',')
    operators = ['+', '-', 'x', '/']

    stack = []
    for char in exp:

        if char in operators:

            x = stack.pop()
            y = stack.pop()

            # compute
            if char == '+':
                stack.append(x+y)
            elif char == '-':
                stack.append(x-y)
            elif char == 'x':
                stack.append(x*y)
            else:
                stack.append(x/y)
        else:
            stack.append(int(char))

    # only one value remaning
    return stack.pop()

exp = '3,4,+,2,x,1,+'
print 'the expression is', exp
print 'the expression evaluates to', evaluateRPN(exp)



