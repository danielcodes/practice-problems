

flat = {}
sample = {
          'Key1': '1',
          'Key2': {
            'a' : '2',
            'b' : '3',
            'c' : {
              'd' : '3',
              'e' : '1'
              }
            }
         }


print 'before', flat

def flattenDict(initKey, dictionary, flatDict):
    
    # gotta iterate through each key
    for key in dictionary.keys():
        
        value = dictionary.get(key)
        # if value is a dict, recurse
        if type(value) is type(dict()):
            # recurse accodingto parent key
            if initKey == '':
                flattenDict(key, value, flatDict)
            else:
                flattenDict(initKey + '.' + key, value, flatDict)
        else: #a primitive
            
            # check for parent
            if initKey == '':
                flatDict.update({key: value})
            else:
                flatDict.update({initKey+'.'+key: value})
            

flattenDict('', sample, flat)
print 'after', flat


