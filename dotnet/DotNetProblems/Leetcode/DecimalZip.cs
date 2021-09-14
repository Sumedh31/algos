using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetProblems.Codelity
{
    class DecimalZip
    {
        public static void Init()
        {
            int number1 = 12300;
            int number2 = 103;
            var result=ZipNumbers(number1, number2);
            Console.WriteLine(result);
            Console.ReadLine();

        }
        static int ZipNumbers(int firstNumber,int secondNumber)
        {
            string numConersion1 = firstNumber.ToString();            
            string numConersion2 = secondNumber.ToString();
            List<int> ListOFDigitsin1 = numConersion1.ToCharArray().Select(x => int.Parse(x.ToString())).ToList();
            List<int> ListOFDigitsin2 = numConersion2.ToCharArray().Select(x => int.Parse(x.ToString())).ToList();
            List<int> output = new List<int>();
            int max=ListOFDigitsin1.Count >= ListOFDigitsin2.Count ? ListOFDigitsin1.Count : ListOFDigitsin2.Count;
            for(int i=0;i<max;i++)
            {
                if (i< ListOFDigitsin1.Count)
                {
                    output.Add(ListOFDigitsin1[i]); 
                }
                if (i < ListOFDigitsin2.Count)
                {
                    output.Add(ListOFDigitsin2[i]);
                }
            }
            string outp= string.Join("",output);
            return int.Parse(outp);
        }
    }
}
