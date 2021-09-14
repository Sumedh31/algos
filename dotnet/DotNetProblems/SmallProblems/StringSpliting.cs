//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class StringSpliting
//    {
//        static void Main(String[] args)
//        {
//            Console.WriteLine("Split with multiple separators");
//            // Split with multiple separators  
//            string multiCharString = "Mahesh..Chand, Henry\n He\t, Chris-Love, Raj..Beniwal, Praveen-Kumar";

//            string[] multiarray = multiCharString.Split(new Char[] { ' ', ',', '.', '-','\n','\t' });
//            foreach (string word in multiarray)
//            {
//                if (word.Trim() != "")
//                    Console.Write(word+" ");
//            }
//            try
//            {
//                int x = Convert.ToInt32(Console.ReadLine());
//                Console.Write(x + 2);
//            }
//            catch (FormatException)
//            {
//                Console.Write("Give correct input");
//            }
            
//            Console.Read();
            

//        }
//    }
//}
