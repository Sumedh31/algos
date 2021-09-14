'''
Created on 24-Jun-2019

@author: Sumedh.Tambe
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def SameLevelTraverse(Root):
    if Root is None:
        return
    Queue=[]
    Queue.append(Root)
    
    while(True):
        Nodecount=len(Queue)
        if(Nodecount==0):
            break 
        
        while(Nodecount>0):
            print(Queue[0].data, end=' ')                
            currentNode=Queue.pop(0)
            if(currentNode.left is not None):
                Queue.append(currentNode.left)
            if(currentNode.right is not None):
                Queue.append(currentNode.right)
            Nodecount-=1   
        print("")  
                
            

if __name__=='__main__':
    Root=Node(2)
    Root.left = Node(1) 
    Root.right = Node(3) 
    Root.left.left = Node(0) 
    Root.left.right = Node(7) 
    Root.right.left=Node(9)
    Root.right.right=Node(1)
    SameLevelTraverse(Root)