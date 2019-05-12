'''
Created on 26-Apr-2019

@author: Sumedh.Tambe
'''
from _collections import defaultdict
class Graph():
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSTraverse(self,v,visited):
        visited[v]=True
        print(v)
        
        for I in self.graph[v]:
            if(visited[I]==False):
                self.DFSTraverse(I, visited)
        
    def DFSInitTraverse(self):
        #Mark all vertices as not visited
        Vertices=len(self.graph)
        visited=[False]*Vertices
        
        for I in range(Vertices):
            if(visited[I]==False):
                self.DFSTraverse(I,visited)
if __name__ == '__main__':
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
      
    #print "Following is Depth First Traversal"
    g.DFSInitTraverse() 