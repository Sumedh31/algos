'''
Created on 06-Apr-2019

@author: Sumedh.Tambe
'''
class StackWithMax: 
    def __init__(self): 
          
        # main stack  
        self.mainStack = []  
      
        # tack to keep track of 
        # max element  
        self.trackStack = [] 
    def Push(self,x):
        self.mainStack.append(x)
        if(len(self.mainStack)==1):            
            self.trackStack.append(x)
            return
        if(x>self.trackStack[-1]):
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])
    def getMax(self):
        return self.trackStack[-1]
if __name__ == '__main__': 
  
    s=StackWithMax()
   
    s.Push(60) 
      
    s.Push(20)
    
    s.Push(50)
      
    print(s.getMax())     