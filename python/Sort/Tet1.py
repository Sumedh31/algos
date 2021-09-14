'''
Created on 20-Jul-2019

@author: Sumedh.Tambe
'''
def solution(X, Y):
    # write your code in Python 3.6
    Mini=0
    Big=0
    gotTheBurger=False
    result=[]
    for I in range(X):
        if(X*2==Y):
            gotTheBurger=True
            Mini=X*2
            Big=Big+0
            break
        else:
            X=X-1
            Y=Y-4
            Big=Big+1
    result.append(Mini)
    result.append(Big)
    if(gotTheBurger==True):
        return result
    else:
        return [-1,-1]
    
if __name__=='__main__':
    X=int(input())
    Y=int(input())
    solution(X,Y)