//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class SecondLowest       
       
//        public static void Main(string[] args)
//        {
//            int [] newArray=new int[5]{1,2,3,4,5};
//            int length = newArray.Length;
//            int m1=100;
//            int m2 = 100;
//            var myDict = new Dictionary<int, int>();
//            myDict.Add(1, 1);
//            for (int index = 0; index < length; index++)
//            {
//                if (m1 > newArray[index])
//                {
//                    m2 = m1;
//                    m1 = newArray[index];                    
//                }
//                else if (m2 > newArray[index] && newArray[index] != m1)
//                {
//                    m2 = newArray[index];
//                }
//            }
//            Console.Write(m2);
//                //foreach (KeyValuePair<int, int> item in myDict)
//                //{
//                //    Console.WriteLine("Key: {0},Value:{1}",item.Key,item.Value);
//                //}
//            Console.Read();
//        }
        

//    }
//}

using System;
using System.Collections.Generic;
using System.Globalization;

namespace DotNetProblems.SmallProblems {
    class SecondLowest{
        public static int GetSecondLowest(int[] arr){
            int lowest =1000;
            int secondLowest = 1000;
            foreach(int num in arr){
                if(num < lowest){
                    secondLowest = lowest;
                    lowest = num;
                }
                else if (num < secondLowest && num > lowest) {
                    secondLowest = num;
                }
            }

            return secondLowest;
        }

        public static void Main(String[] args) {
        }  
    }

}
