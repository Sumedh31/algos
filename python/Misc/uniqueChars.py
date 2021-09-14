'''
Created on 20-May-2019

@author: Sumedh.Tambe
'''

def printUniqueChars(listIn):
    dicUniqueChar={}
    for char in listIn:
        if(char in dicUniqueChar.keys()):
            dicUniqueChar[char]+=1
        else:
            dicUniqueChar[char]=1
    for key in dicUniqueChar.keys():
        print(key)      


if __name__ == '__main__':
    inputString=input()
    listInput=[]
    for char in inputString:
        if char not in listInput:
            listInput.append(char)
    print(listInput)
        