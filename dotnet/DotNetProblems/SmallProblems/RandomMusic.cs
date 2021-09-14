//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class RandomMusic
//    {
//        static void Main(String[] args)
//        {
//            Random random = new Random();
//            List<int> files = new List<int> { 1, 2, 3, 4 };
//            for(int i=0;i<files.Count;i++)
//            {
//                int number=random.Next(files.Count);
//                int temp = files[i];
//                files[i]=files[number];
//                files[number] = temp;
//            }
//            foreach(int ele in files)
//                Console.Write(ele);
//            Console.Read();
//        }
//    }
//}
