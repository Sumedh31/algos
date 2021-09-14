//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SearchStrings
//{
//    class PatternSearchingNaive
//    {
//        static void Search(string pat, string txt)
//        {
//            int lenofpattern = pat.Length;
//            int lenoftxt = txt.Length;
//            for (int i = 0; i < (lenoftxt - lenofpattern); i++)
//            {
//                int counter = 0;
//                for (int j = 0; j < lenofpattern; j++)
//                {
//                    if (txt[i + j] != pat[j])
//                        break;
//                    counter += 1;
//                }
//                if (counter == lenofpattern)
//                    Console.Write("Found at index"+i+"\n");
                
//            }
//            Console.Read();
//        }
//        static void Main(String[] args)
//        {
//            string  text= "AABAACAADAABAAABAA";
//            string  pattern= "AABA";
//            Search(pattern, text);
//        }
//    }
//}
