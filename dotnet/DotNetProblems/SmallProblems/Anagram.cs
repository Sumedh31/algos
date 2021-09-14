using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicecoding.Misc
{
    class Anagram
    {
        public static void Init()
        {
            string in1 = "tAtA";
            StringBuilder output = new StringBuilder();
            foreach (Char chr in in1)
            {
                if (Char.IsLower(chr))
                {
                    output.Append(Char.ToUpper(chr));
                }
                else
                {
                    output.Append(Char.ToLower(chr));
                }
            }
            Console.WriteLine(output);
            Console.Read();


        }
    }
}
