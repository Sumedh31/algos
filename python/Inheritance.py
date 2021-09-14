class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Summation(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Summation1(self, a, b):
        return a-b
d = Derived()  
print(d.Summation(10, 20))