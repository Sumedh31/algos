'''
Created on 10-Jul-2019

@author: Sumedh.Tambe

list=[11,23,45,32] 32,45,23,11 
'''
# 
# inputList=[11,23,45,32]
def reverseTheList(List):
    length=len(List)
    reversed=[]
     
    for I in range(length-1,-1,-1):
         
        reversed.append(List[I])
    return reversed

str1='Mathematics'
str2='malayalam'

strToList=list(str2)
rev=reverseTheList(strToList)
print(rev)
if(strToList==reverseTheList(strToList)):
    print("Yes Palindrome")
else:
    print("No palindrome")