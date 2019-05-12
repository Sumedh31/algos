'''
Created on 20-Apr-2019

@author: Sumedh.Tambe
'''
class Node: 
    # A utility function to create a new node 
    def __init__(self ,key): 
        self.Data = key 
        self.Left = None
        self.Right = None
  

def NodesFromSameHeight(Root): 
    
    if Root is None: 
        return     
    
    Queue = []  
    
    Queue.append(Root) 
    while(True):
        NodeCount=len(Queue)   
        if(NodeCount==0):
            break 
          
        while(NodeCount > 0): 
                        
            print ("(%d)"%Queue[0].Data,end=", ") 
            
            CurrentNode = Queue.pop(0)   
            
            if CurrentNode.Left is not None: 
                Queue.append(CurrentNode.Left)      
             
            if CurrentNode.Right is not None: 
                Queue.append(CurrentNode.Right) 
            NodeCount-=1
        print(" ")
  
if __name__ == '__main__':
    
    Root = Node(2) 
    Root.Left = Node(1) 
    Root.Right = Node(3) 
    Root.Left.Left = Node(0) 
    Root.Left.Right = Node(7) 
    Root.Right.Left=Node(9)
    Root.Right.Right=Node(1)
    NodesFromSameHeight(Root) 
