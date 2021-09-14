////Find all strings that match specific pattern in a dictionary
////Input:  
////dict = ["abb", "abc", "xyz", "xyy"];
////pattern = "foo"
////Output: [xyy abb]
////Explanation: 
////xyy and abb have same character at index 1 and 2 like the pattern

//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SearchStrings
//{
//    class SpecificPatternInDict
//    {
//        static String encodedString(String str)
//        {
//            Dictionary<char, int> map = new Dictionary<char, int>();
//            String res = "";
//            int i = 0;
//            char ch;
             

//            for (int j = 0; j < str.Length; j++)
//            {
//                ch=str[j];
//                if(!map.ContainsKey(ch))
//                    map.Add(ch,i++);
//                res = res+map[ch];
//            }
//            return res;
//        }
//        static void MatchedWords(String[] dict, String Pattern)
//        {
//            int len = Pattern.Length;

//            String hash = encodedString(Pattern);
//            foreach (String Word in dict)
//            {
//                if (Word.Length == len && encodedString(Word).Equals(hash))
//                    Console.Write(Word + " ");
//            }
//            Console.Read();
//        }
//        public static void Main(string[] args)
//        {
//            String[] dict = { "abb", "abc", "xyz", "xyy" };
//            String pattern = "foo";
//            MatchedWords(dict,pattern);
//        }
//    }
//}
