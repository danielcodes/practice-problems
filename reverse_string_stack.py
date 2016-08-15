
# use a stack to reverse a string

# runs in O(n) 
def reverseStack(string):
    
    stack = []
    for c in string:
        stack.append(c)

    print stack

    # can't do character assignment on string, so adding it
    # to a new variable
    result = ''
    for i in range(len(stack)):
        result += stack.pop()

    print result


user_input = raw_input('enter a string, ')
reverseStack(user_input)



