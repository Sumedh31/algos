//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class maxUsingStack
//    {
//        static void Main(String[] args)
//        {
//            Stack<int> mainStack = new Stack<int>();
//            Stack<int> trackStack = new Stack<int>();

//            mainStack.Push(60);
//            mainStack.Push(20);
//            mainStack.Push(20);
//            mainStack.Push(90);
//            mainStack.Push(80);
//            mainStack.Push(30);
//            if (trackStack.Count == 0)
//            {
//                trackStack.Push(mainStack.Pop());
//            }
//            for (int i = 0; i < mainStack.Count; i++)
//            {
//                if (mainStack.Peek() >= trackStack.Peek())
//                {
//                    trackStack.Pop();
//                    trackStack.Push(mainStack.Pop());
//                }
//            }
           
//            Console.Write("Max is" + trackStack.Peek());
//            Console.Read();
            
//        }
//    }
//}
