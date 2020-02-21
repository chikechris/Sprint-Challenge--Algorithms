'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "algorithmathicthddth"

def count_th(word):
  
    # If word is empty, return 0 for false
    if word == '':
        return 0

    else:
        # if the string 'th' is in 'word
        if word[0:2] == 'th':
            # return 1 and increment 2 indecies and recursively run the function
            return 1 + count_th(word[2:])
        else:
            # don't return anything and increment 1 index and recursively run the function
            return count_th(word[1:])

print(count_th(word))            
       


    
    
    
