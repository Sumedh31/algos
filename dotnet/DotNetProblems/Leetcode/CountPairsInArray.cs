using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetProblems.Codelity
{
    class CountPairsInArray
    {
        public static void Init()
        {
            int[] given = new int[] { 1, 1, 1, 1, 2, 3, 2, 4 };
            var result= GetPairs(given);
            Console.WriteLine(result);
            Console.Read();
        }
        static int GetPairs(Array input)
        {
            Dictionary<int, int> mapping = new Dictionary<int, int>();
            int pair = 0;
            foreach (int item in input)
            {
                if(mapping.ContainsKey(item))
                {
                    mapping[item] += 1;
                    if(mapping[item]%2==0)
                    {
                        pair += 1;
                    }
                }
                else
                {
                    mapping[item] = 1;
                }
            }
            return pair;
        }
    }
}
