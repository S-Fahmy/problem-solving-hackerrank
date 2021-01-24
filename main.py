#!/bin/python3


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
import string

def authEvents(events):
    # Write your code here
    passwordString = ''
    hashedPassword = 0
    solutionsList = []
    
    print(events)
    
    for event in events:
        if event[0] == 'setPassword' :
            #setpassword string
            passwordString = event[1]
            
            #hash it
            hashedPassword = hashPassword('cAr1')
            
            print(event[1])
            
        elif event[0] == 'authorize':
            print(event[1])
            if event[1] == hashedPassword or isHashedPasswordWithExtraCharacter(passwordString,hashedPassword ,event[1]):
                solutionsList.append(1)
            else:
                solutionsList.append(0)
                
                
    return solutionsList

            
def isHashedPasswordWithExtraCharacter(password, hashedPassword, authHashedPassword):
    #generate a list of alphabets and digits 0-9
    alphs = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    
    for c in alphs:
        
        pswdHashWithExtraChr = hashPassword(password+c)    
        if pswdHashWithExtraChr == authHashedPassword:
            return True
            
            
            

def hashPassword(passwordString):
    #loop through each password character and apply the formula
    p = 131
    M = 10**9 + 7
    i = 1
    hashingInt = 0
    for c in passwordString:
        #print(c +' '+ str(ord(c))+ ' ' + str(len(passwordString)-i))
        hashingInt += ord(c)*(p**(len(passwordString)-i))
        i +=1
        
    hashingInt = hashingInt % M
    
    print(hashingInt)
    return hashingInt
        
if __name__ == '__main__':
    
    authEvents([['setPassword', 'cArs1'], ['authorize', '88']]) #correct values to be put here via hackerrank