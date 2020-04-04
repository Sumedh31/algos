'''
Created on 10-Apr-2019

@author: Sumedh.Tambe
'''
from _collections import OrderedDict
def Access(key,LRUDict):
    
    if(len(LRUDict)==5):
        LRUDict.popitem()
                      
                   
    if key in LRUDict.keys():
            LRUDict.move_to_end(key, last=False)
    else:
        LRUDict[key]=''
        LRUDict.move_to_end(key,last=False)  
    print(LRUDict)  
    return list(LRUDict)[0] 
        
if __name__ == '__main__':
    LRUDict=OrderedDict()
    print(Access(20,LRUDict))
    print(Access(30,LRUDict))
    print(Access(40,LRUDict))
    print(Access(50,LRUDict))
    print(Access(60,LRUDict))
    print(Access(70,LRUDict))
    print(Access(30,LRUDict))
    
    