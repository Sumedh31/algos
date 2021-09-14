//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.Trees
//{
//    class Node
//    {
//        public int key;
//        public Node left, right;

//        public Node(int item)
//        {
//            key = item;
//            left = right = null;
//        }
        
//    }
//    class bfsForTree
//    {
//        Node root;
//        public bfsForTree()
//        {
//            root = null;
//        }
//        void InorderTraversal(Node node)
//        {
//            if (node != null)
//            {
//                InorderTraversal(node.left);

//                Console.Write(node.key+" ");

//                InorderTraversal(node.right);
//            }
//        }
//        void PreorderTraversal(Node node)
//        {
//            if (node != null)
//            {
//                Console.Write(node.key + " ");

//                PreorderTraversal(node.left);

//                PreorderTraversal(node.right);
//            }
//        }
//        void PostOrderTraversal(Node node)
//        {
//            if (node != null)
//            {
//                PostOrderTraversal(node.left);

//                PostOrderTraversal(node.right);

//                Console.Write(node.key + " ");

//            }
//        }
//        static void Main(String[] args)
//        {
//            bfsForTree tree = new bfsForTree();
//            tree.root = new Node(1);
//            tree.root.left = new Node(2);
//            tree.root.right = new Node(3);
//            tree.root.left.left = new Node(4);
//            tree.root.left.right = new Node(5);
//            tree.InorderTraversal(tree.root);
//            Console.Write("Post order");
//            tree.PostOrderTraversal(tree.root);
//            Console.Write("pre order");
//            tree.PreorderTraversal(tree.root);
//            Console.Read();
            
//        }
//    }
//}
