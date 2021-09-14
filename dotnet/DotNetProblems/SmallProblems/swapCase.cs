//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class swapCase
//    {
//        public static void Main(String[] args)
//        {
//            string str1 = "This is Good";
//            byte[] AsciiValues = Encoding.ASCII.GetBytes(str1);
//            char[] splichar = {' '};
//            var str2 = str1.Split(splichar);
//            Console.Write(str1[0]);

//            string reversed = new string(
//                                        str1.Select(c=>char.IsLetter(c) ? (char.IsUpper(c) ?
//                                                        char.ToLower(c):char.ToUpper(c)):c).ToArray());
//            Console.Write(reversed);
//                //foreach (string item in str2)
//                //{
//                //    Console.Write(item+" ");
//                //}
//                Console.Read();

//        }
//    }
//}
