using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace DotNetProblems.SmallProblems
{
    class GetAllPermutations
    {
        GetAllPermutations()
        {

        }
        public static void Init()
        {
            string input = "ABC";
            List<string> storage = new List<string>();
            int currentstep = 0;
            getPermuatations(input, currentstep);

        }
        static void getPermuatations(string input,int currentstep)
        {
            string givenString = "";
            if(currentstep==input.Length)
            {
                Console.WriteLine(input);
                Console.ReadLine();
            }
            for (int i=currentstep;i< input.Length;i++)
            {
                char [] chararr = input.ToCharArray();
                char temp = chararr[currentstep];
                chararr[currentstep] = chararr[i];
                chararr[i] = temp;
                getPermuatations(new string(chararr),currentstep+1);

            }
        }
    }
}
