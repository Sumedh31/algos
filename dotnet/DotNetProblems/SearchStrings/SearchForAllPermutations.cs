//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SearchStrings
//{
//    class SearchForAllPermutations
//    {
//        public const int Max = 256;
//        public static bool Compare(char[] arr1, char[] arr2)
//        {
//            for (int index = 0; index < Max; index++)
//            {
//                if (arr1[index] != arr2[index])
//                {
//                    return false;
//                }               
//            }
//            return true;
//        }
//        public static void Search(string pat, string txt)
//        {
//            int M = pat.Length;
//            int N = txt.Length;
//            char[] countP = new char[Max];
//            char[] countTW = new char[Max];
//            for (int i = 0; i < M; i++)
//            {
//                (countP[pat[i]])++;
//                (countTW[pat[i]])++;
//            }
//            for (int i = M; i < N; i++)
//            {
//                if (Compare(countP, countTW))
//                {
//                    Console.WriteLine("Found at index " + (i - M));
//                }
//                (countTW[txt[i]])++;
//                countTW[txt[i-M]]--;
               
//            }
//            if (Compare(countP, countTW))
//            {
//                Console.WriteLine("Found at index " + (N - M));
//                Console.Read();
//            }
//        }
//        public static void Main(String[] args)
//        {
//            string txt = "BACDGABCDA";
//            string pat = "ABCD";
//            Search(pat, txt); 
//        }
//    }
//}
