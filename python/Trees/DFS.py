class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None
def PrintInOrder(root):
    if root:        
        PrintInOrder(root.left)
        
        PrintInOrder(root.Right)
        
        print(root.data)

if __name__=='__main__':
    root=Node(1)
    root.left=Node(2)
    root.Right=Node(3)
    root.left.left=Node(4)
    root.left.Right=Node(5)
    PrintInOrder(root)
    
    
        