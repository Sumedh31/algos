'''
Created on 18-Jan-2021

@author: sumedh
Given a string, find max occurred character in it. If found multiple character with same number of 
occurrence then return the first occurred character from string
E.g if str="abbcc" then return b =2 occurrence
'''
#Brute force
str="hello world"

# Max=0
# MaxChar=""
# 
# for char in str:
#     if(str.count(char)>Max):
#         Max=str.count(char)
#         MaxChar=char
#         
# print(MaxChar)

#Efficient
Max=0
MaxChar=""
prevPos=0
CharCount={}
for pos,char in enumerate(str):
    if(char in CharCount.keys()):
        CharCount[char][1]+=1
    else:
        CharCount[char]=[pos,1]
for key in CharCount.keys():
    if(CharCount[key][1]>Max):
        Max=CharCount[key][1]
        MaxChar=key
        prevPos=CharCount[key][0]
    elif(CharCount[key][1]==Max):
        if(CharCount[key][0]<prevPos):
            prevPos=CharCount[key][0]
            MaxChar=key
print(MaxChar,Max)
        
    
