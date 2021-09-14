'''
Created on 12-May-2019

@author: Sumedh.Tambe
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    ListOfDigitsInA=[int(d) for d in str(A)]
    ListOfDigitsInB=[int(d) for d in str(B)]
    DecimalZip=[]
     
    if(len(ListOfDigitsInA)>=len(ListOfDigitsInB)):
        Max=len(ListOfDigitsInA)
    else:
        Max=len(ListOfDigitsInB)
     
    for I in range(Max):
        if(len(ListOfDigitsInA)>I):            
            DecimalZip.append(ListOfDigitsInA[I])
        if(len(ListOfDigitsInB)>I):
            DecimalZip.append(ListOfDigitsInB[I])
     
    DecimalZipNumber=''.join(str(x) for x in DecimalZip)
     
    if(int(DecimalZipNumber)>=100000000):
        return -1
    else:
        return int(DecimalZipNumber)
         
if __name__ == '__main__':
    A=123000
    B=0
    print(solution(A,B))