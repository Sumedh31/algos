'''
Created on 10-Jul-2019

@author: Sumedh.Tambe Make the permutations of given string
'''
from pip._vendor.msgpack.fallback import xrange

# def toString(List):
#     return ''.join(List)
# def permutate(listofChar,start,len):
#     if(start==len):
#         print(toString(listofChar))
#     else:
#         for i in xrange(start,len):
#             listofChar[start],listofChar[i]=listofChar[i],listofChar[start]
#             permutate(listofChar, start+1, len)
#             listofChar[start],listofChar[i]=listofChar[i],listofChar[start]
# givenstr='ABC'
# listStr=list(givenstr)
# permutate(listStr, 0, len(listStr)-1)

def getPermutations(inputstr,currentstep):
    allPerm=[]
    if(currentstep==len(inputstr)):
        #allPerm.append(inputstr)
        print("".join(inputstr))
    for i in range(currentstep,len(str)):
        getChar=[char for char in inputstr]
        print("The current string array is",getChar, " index is ", i ," Currentstep",currentstep,"swapping", getChar[currentstep],"with", getChar[i])
        temp=getChar[currentstep]
        getChar[currentstep]=getChar[i]
        getChar[i]=temp
        getPermutations(getChar,currentstep+1)
    
if __name__ == '__main__':    
    getPermutations("ABC",0)
    
        
        
        
        
    