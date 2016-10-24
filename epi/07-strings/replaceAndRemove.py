
# replace and remove
# given a string, apply two rules
# replace 'a's with 'dd's and remove all 'b's 
# given the array and size, the length of input to be operated on 

# acdbbca => ddcdcdd

# for the future, turn strings to array of chars

def replaceAndRemove(string, size):
    
    # approach is to first remove b's and keep a count on the a's 
    # first iter, acdbbca -> acdca__ 
    write_idx = 0
    a_count = 0
    string = list(string)
    
    for i in range(size):
        
        # can't do string assignemnt since str are immutable
        # have to create new string 
        if string[i] != 'b':
            string[write_idx] = string[i]
            write_idx += 1
        
        if string[i] == 'a':
            a_count += 1
    
    # print string
    # print a_count, write_idx
    
    # second iter, iterate backwards and start replacing a's with 2 d's 
    cur_idx = write_idx - 1
    write_idx = write_idx + a_count - 1
    
    while cur_idx >= 0:
        
        if string[cur_idx] == 'a':
            string[write_idx] = 'd'
            write_idx -= 1
            string[write_idx] = 'd'
            write_idx -= 1
        else:
            string[write_idx] = string[cur_idx]
            write_idx -= 1
        
        cur_idx -= 1
    
    # print write_idx, cur_idx, string
    
    return ''.join(string)
            
    
string = 'acdbbca'
print 'before replace and remove', string
print 'after replace and remove ', replaceAndRemove(string, 7)


