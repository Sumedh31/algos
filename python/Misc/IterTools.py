'''
Created on 12-May-2019

@author: Sumedh.Tambe
'''
import itertools
 
L = ['a','b','c']
c = []
 
for i in range(1, len(L)+1):
    l = [list(x) for x in itertools.combinations(L, i)]
    c.extend(l)
d=[]
l = [list(x) for x in itertools.combinations(L, 2)]
d.extend(l)
x= (int(len(c)) + int(len(d)))
print(x)
def example(L):
    ''' (list) -> list
    '''
    i = 1
    result = []
    while i < len(L):
        result.append(L[i])
        print (result)
        i = i + 3
    return result
 
print(example([1,2,3,4,5]))