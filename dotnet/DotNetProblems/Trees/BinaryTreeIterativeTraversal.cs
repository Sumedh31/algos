using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetProblems.Trees
{
    class Node
    {
        public int data;
        public Node right;
        public Node left;
        public Node(int data)
        {
            this.data = data;
            this.right = null;
            this.left = null;
        }
    }
    class BinaryTreeIterativeTraversal
    {
        public Node root;
        public static void Init()
        {
            BinaryTreeIterativeTraversal tree = new BinaryTreeIterativeTraversal();
            tree.root = new Node(1);
            tree.root.left = new Node(2);
            tree.root.right = new Node(3);
            tree.root.left.left = new Node(4);
            tree.root.left.right = new Node(5);
            IterativeInorder(tree.root);
            IterativePostorder(tree.root);
            IterativePreorder(tree.root);


        }
        private static void IterativeInorder(Node root)
        {
            Stack<Node> maintainer = new Stack<Node>();
            Node current = root;
                      
            while(true)
            {
                if(current!=null)
                {
                    maintainer.Push(current);
                    current = current.left;
                }
                else if(maintainer.Count>0)
                {                    
                    current = maintainer.Pop(); 
                    Console.WriteLine(current.data + " ");
                    //if (current.right == null)
                    //    current = null;
                    //else
                    current = current.right;
                }
                else
                {
                    Console.ReadLine();
                    break;
                }
                        
            }
        }
        public static void IterativePostorder(Node root)
        {
            Stack<Node> stack1 = new Stack<Node>();
            Stack<Node> stack2 = new Stack<Node>();

            if (root == null)
                return;
            stack1.Push(root);
            while(stack1.Count>0)
            {
                var current = stack1.Pop();
                stack2.Push(current);
                if (current.left != null)
                    stack1.Push(current.left);
                if (current.right != null)
                    stack1.Push(current.right);
            }
            while(stack2.Count>0)
            {
                var node = stack2.Pop();
                Console.Write(node.data+" ");
            }
            Console.Read();
        }
        public static void IterativePreorder(Node root)
        {
            Stack<Node> nodestack = new Stack<Node>();
            if (root == null)
                return;
            nodestack.Push(root);
            while(nodestack.Count>0)
            {
                var current = nodestack.Pop();
                Console.WriteLine(current.data);
                if (current.right != null)
                    nodestack.Push(current.right);
                if(current.left != null)
                    nodestack.Push(current.left);
            }
            Console.Read();
        }
    }
}
