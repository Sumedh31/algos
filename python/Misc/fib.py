'''
Created on 11-Jun-2019

@author: Sumedh.Tambe
'''
numberFib=int(input("Give number =  "))

a=0
b=1

for I in range(numberFib):
    if(I==0):
        print(0,end=' ')
    elif(I==1):
        print(1,end=' ')
    else:
        c=a+b
        a=b
        b=c
        print(b,end=' ')