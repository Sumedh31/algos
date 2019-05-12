'''
Created on 21-Apr-2019

@author: Sumedh.Tambe
'''
def Fibonacci(Number):
    a=0
    b=1    
    if(Number==1):
        return 0
    elif(Number==2):
        return 1
    else:
        for I in range(2,Number):
            c=a+b
            a=b
            b=c
        return b
        
    
if __name__ == '__main__':
    Number=int(input())
    print(Fibonacci(Number))
    