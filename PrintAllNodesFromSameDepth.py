'''
Created on 16-Apr-2019

@author: Sumedh.Tambe
'''
from _collections import OrderedDict
class RootData(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def traversetree(root,hd,level,m):
    if root:
        if hd in m:
            m.update({hd:[root.data,level]})  
        else:
            
            m[hd]=[root.data,level]  
        #print(root.data)
        traversetree(root.left,hd-1,level+1,m)
        traversetree(root.right,hd+1,level+1,m)
def PrintSameLevelNode(root):
    hd=0
    level=0
    m=OrderedDict()
    traversetree(root,hd,level,m)
    for data in m:
        print(m[0][1])
    

if __name__ == '__main__':
    hd=0
    level=0
    root=RootData(2)
    root.left=RootData(1)
    root.left.left=RootData(0)
    root.left.right=RootData(7)
    root.right=RootData(3)
    root.right.left=RootData(9)
    root.right.right=RootData(1)
    PrintSameLevelNode(root)