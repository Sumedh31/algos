'''
Created on 15-Jun-2020

@author: Sumedh
'''
from ctypes.wintypes import CHAR

def getPermutations(str,currentstep):
    allperm=[]
    if(currentstep==len(str)):
        print("".join(str))
    for i in range(currentstep,len(str)):
        charhold=[char for char in str]
        temp=charhold[currentstep]
        charhold[currentstep]=charhold[i]
        charhold[i]=temp
        getPermutations(charhold,currentstep+1)
if __name__ == '__main__':
    getPermutations("ABC",0)
