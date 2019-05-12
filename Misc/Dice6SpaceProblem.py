'''
Created on 21-Apr-2019

@author: Sumedh.Tambe

 Imagine you are playing a board game. You roll a 6-faced dice and 
 move forward the same number of spaces that you rolled. If the finishing point is n spaces 
 away from the starting point, please implement a program that calculates how many possible 
 ways there are to arrive exactly at the finishing point.
 
 f(6)=f(5)+f(4)....+f(1)+f(0)
 f(1)=f(0)=1,f(2)=f(1)+f(0)=2....
'''

def PossibleWaysUsingHexanacciSeries(Number):
    FirstStep=0
    SecondStep=0
    ThirdStep=0
    FourthStep=0
    FifthStep=0
    SixthStep=1
    for I in range(0,Number+1):
        ways=FirstStep+SecondStep+ThirdStep+FourthStep+FifthStep+SixthStep
        if(I>0):
            FirstStep=SecondStep
            SecondStep=ThirdStep
            ThirdStep=FourthStep
            FourthStep=FifthStep
            FifthStep=SixthStep
            SixthStep=ways            
    return ways
if __name__=='__main__':
    NoOfSteps=int(input())
    Totalways=PossibleWaysUsingHexanacciSeries(NoOfSteps)
    print(Totalways)
    
            
    

