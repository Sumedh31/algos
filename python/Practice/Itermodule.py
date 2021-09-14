'''
Created on 23-Jun-2019

@author: Sumedh.Tambe
'''
class printNumber():
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        if(self.num>=self.max):
            raise StopIteration
        self.num+=1
        return self.num
printnum=printNumber(3)
myIter=iter(printnum)

print(next(myIter))