using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicecoding.Misc
{
    class GetSubstrings
    {
        GetSubstrings()
        {

        }
        static void Init()
        {
            var str = "ABCD";
            GetSubstrings obj = new GetSubstrings();
            obj.GetSubStrings(str, str.Length);

        }
        void GetSubStrings(String str, Int32 len)
        {
            int substringLen = len;
            for (int i = 0; i < len; i++)
            {

                for (int j = 1; j <= substringLen; j++)
                {
                    var newstr = str.Substring(i, j);
                    Console.WriteLine(str.Substring(i, j));
                }
                substringLen -= 1;

            }
        }
    }
}
