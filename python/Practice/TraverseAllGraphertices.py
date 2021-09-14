'''
Created on 11-Jul-2019

@author: Sumedh.Tambe
'''
from _collections import defaultdict
class graph():
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,vertice,edge):
        self.graph[vertice].append(edge)
    
    def DFSTraverse(self,vertice,visited):
        visited[vertice]=True
        print(vertice)
        
        for i in self.graph[vertice]:
            if(visited[i]==False):
                self.DFSTraverse(i, visited)
    def InitTraverse(self,vertice):
                
        noOfVertices=len(self.graph)
        visited=[False]*noOfVertices
        
#         for i in range(noOfVertices):
#             if(visited[i]==False):
        self.DFSTraverse(vertice,visited)
if __name__ == '__main__':
    g = graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
      
    #print "Following is Depth First Traversal"
    g.InitTraverse() 