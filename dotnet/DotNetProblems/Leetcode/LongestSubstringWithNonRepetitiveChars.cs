using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace DotNetProblems.Leetcode
{
    public class LongestSubstringWithNonRepetitiveChars
    {
        public static void Init()
        {
            string given = "abcabcbb";
            string result=getAllSubStrings(given);
            Console.WriteLine("The result is -"+result);
            Console.ReadKey();
        }
        public static string getAllSubStrings(string given)
        {
            string maxlen = "";
            int counterLength = given.Length;
            List<string> allsubs = new List<string>();
            for(int i=0;i<given.Length;i++)
            {
                for (int j = 1; j <= counterLength; j++)
                {
                    string current = given.Substring(i, j);
                    if(current.Length>maxlen.Length && isAllunique(current))
                    {
                        maxlen = current;
                    }
                    allsubs.Add(current);
                }
                counterLength--;
            }
                

            return maxlen;
        }
        public static bool isAllunique(string input)
        {
            ArrayList plcholder = new ArrayList();
            foreach(Char chr in input)
            {
                if(plcholder.Contains(chr))
                {
                    return false;
                }
                else
                {
                    plcholder.Add(chr);
                }
            }
            return true;
            
        }
    }
}
