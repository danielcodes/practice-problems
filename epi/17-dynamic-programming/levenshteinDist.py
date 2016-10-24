
# levenshtein distance between two strings
# finding the number of edits needed to convert string A to string B 
# edits include, deleting, inserting and substituting a char 

# approach, use a bottom up table to build up to the solution

def editDistance(a, b):

    m = len(a)
    n = len(b)
    
    # we need a table with the additional row and col
    table = [ [0]*(n+1) for i in range(m+1) ]
    
    # extra row and col
    for i in range(m+1):
        for j in range(n+1):
                
            # two base cases
            # takes care of the one of the strings is empty
            # which means that it's either delete all or insert all
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif a[i-1] == b[j-1]:
                # range's last value is non-inclusive, but we're adding one
                # so we have to do a -1 to prevent going out of range
                # basically, ok for the table, not ok for the string
                # same letter, no cost
                table[i][j] = table[i-1][j-1]
            else:
                # cost of 1 + the min between 3 cases
                # add, delete or substitute
                lesserDist = min(table[i-1][j-1], table[i-1][j], table[i][j-1])
                table[i][j] = 1 + lesserDist

    for row in table:
        print row
            
    return table[m][n]
	
	
print 'edits needed to change three to tres\n', editDistance('three', 'tres')
print 'edits needed to change Saturday to Sundays\n', editDistance('Saturday', 'Sundays')


