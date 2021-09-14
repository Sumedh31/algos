'''
Created on 26-Apr-2019

@author: Sumedh.Tambe

'''
from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph=f=defaultdict(list)
    def Addedge(self,u,v):
        self.graph[u].append(v)
    
    def DFSTraversal(self,u,visited):
        #We will mark the current node as visited
        visited[u]=True
        print(u)
        for I in self.graph[u]:
            if(visited[I]==False):
                self.DFSTraversal(I, visited)              
                
            
    def DFSStartTraverse(self,v):
        #First mark all the vertices as not traversed
        visited=[False]*(len(self.graph))
        #Now start with v as first point
        self.DFSTraversal(v,visited)
        

if __name__ == '__main__':
    g=Graph()
    g.Addedge(0, 1)
    g.Addedge(0, 2)
    g.Addedge(1, 2)
    g.Addedge(2, 0)
    g.Addedge(2, 3)
    g.Addedge(3, 3)
    
    g.DFSStartTraverse(2) 
        