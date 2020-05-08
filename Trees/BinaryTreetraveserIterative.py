'''
Created on 07-May-2020

@author: Sumedh
""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """
      Inorder 42513
            1. Traverse the left subtree, i.e., call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, i.e., call Inorder(right-subtree)
      preorder 12453
            1. Visit the root.
            2. Traverse the left subtree, i.e., call Preorder(left-subtree)
            3. Traverse the right subtree, i.e., call Preorder(right-subtree) 
      postorder 45231 
           1. Traverse the left subtree, i.e., call Postorder(left-subtree)
           2. Traverse the right subtree, i.e., call Postorder(right-subtree)
           3. Visit the root.
'''
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def IterativeInorderTraversal(root):
    maintainer=[]
    currentRoot=root
    while True:
        if(currentRoot is not None):
            maintainer.append(currentRoot)
            currentRoot=currentRoot.left
        elif(maintainer):
            currentRoot=maintainer.pop()
            print(currentRoot.data,end=" ")
            currentRoot=currentRoot.right
        else:
            break
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
IterativeInorderTraversal(root)