'''
Created on 28-Apr-2020

@author: Sumedh
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def printinorder(root):
    if root:
#         print("the current step is ",currentstep)
        printinorder(root.left)
#         print("reach of left end")
#         currentstep=0
        printinorder(root.right)
#         print("reach of right end")
        print(root.data)
Root=Node(1)
Root.left=Node(2)
Root.right=Node(3)
Root.left.left=Node(4)
Root.left.right=Node(5)
printinorder(Root)