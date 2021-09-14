'''
Created on 04-Apr-2020

@author: Sumedh
'''
class Node():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None    

class LRUCache():    
    maps={}
    def __init__(self,capacity):
        self.capacity=capacity
        self.head=Node(None,None)
        self.tail=Node(None,None)
    def removeNode(self,Node):
        if(Node.prev.key!=None):
            Node.prev.next=Node.next
        else:
            self.head=Node.next
        if(Node.next!=None):
            Node.next.prev=Node.prev
        else:
            self.tail=Node.prev          
        
    def insertNode(self,Node):
        if(self.tail.key!=None):
            self.tail.next=Node
        Node.prev=self.tail
        Node.next=None
        self.tail=Node
        if(self.head.key==None):
            self.head=self.tail       

    def get(self,key):
        if key not in self.maps:
            return -1
        referNode=self.maps.get(key)
        self.removeNode(referNode)
        self.insertNode(referNode)
        return referNode.value                            
                
    def put(self,key,value):
        if key in self.maps:
            referNode=self.maps.get(key)
            self.removeNode(referNode)
            self.insertNode(referNode)
        else:
            if(len(self.maps)>=self.capacity):
                self.maps.pop(self.head.key)
                self.removeNode(self.head)
            referNode=Node(key,value)
            self.insertNode(referNode)
            self.maps[key]=referNode
            
            
cache=LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(2,2)
print(cache.get(2))
print(cache.get(1))