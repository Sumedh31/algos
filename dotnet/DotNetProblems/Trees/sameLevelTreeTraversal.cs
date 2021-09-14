//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.Trees
//{
//    class Node
//    {
//        public int data;
//        public Node left, right;
//        public Node(int item)
//        {
//            data = item;
//            left = right = null;
//        }
//    }
//    class sameLevelTreeTraversal
//    {
//        Node root;
//        void SamelevelTraversal(Node node)
//        {
//            Queue<Node> store = new Queue<Node>();

//            if (node == null)
//                return;
//           store.Enqueue(node);
//           while (true)
//           {
//               int NodeCount = store.Count;
//               if (NodeCount == 0)
//                   return;
//               while (NodeCount > 0)
//               {
//                   Console.Write(store.Peek().data + " ");
//                   Node currentNode = store.Dequeue();

//                   if (currentNode.left != null)
//                   {
//                       store.Enqueue(currentNode.left);
//                   }
//                   if (currentNode.right != null)
//                       store.Enqueue(currentNode.right);
//                   NodeCount--;
//               }
//           }


//        }
//        static void Main()
//        {
//            sameLevelTreeTraversal  tree = new sameLevelTreeTraversal();
//            tree.root = new Node(2);
//            tree.root.left=new Node(1);
//            tree.root.right=new Node(3);
//            tree.root.left.left=new Node(0);
//            tree.root.left.right=new Node(7);            
//            tree.root.right.left=new Node(9);
//            tree.root.right.right=new Node(1);
//            tree.SamelevelTraversal(tree.root);
//            Console.Read();


//        }
//    }
//}
