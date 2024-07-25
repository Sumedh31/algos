//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.SmallProblems
//{
//    class fibonacci
//    {
//        static void Main()
//        {
//            int number = 9;
//            int a=0;
//            int b=1;
//            for (int i = 0; i <= number;i++ )
//            {
//                if (i == 0)
//                    Console.Write(i + " ");
//                if (i == 1)
//                    Console.Write(i + " ");
//                else
//                {
//                    int c = a + b;
//                    a = b;
//                    b = c;
//                    Console.Write(b + " ");
//                }
//            }
//            Console.Read();
//        }
//    }
//}
using System;
using System.Collections.Generic;
using System.Globalization;

namespace TestProject1 {
public class Execution
{
    public List<int> GetFibonacci(int n) {
        List<int> series = new List<int>();
        int first =0, second =1, next;
        series.Add(0);
        series.Add(1);

        for(int i =2; i<n; i++){
            next = first + second;
            series.Add(next);
            first = second;
            second = next;
        }
        return series;
    }

    public void PrintFibonacci(){
        List<int> series = this.GetFibonacci(4);
        foreach(int num in series){
            Console.WriteLine(num);
        }
    }

    public static void Main()
    {
        Execution exec = new Execution();
        Console.WriteLine("Fibonacci - ");
        exec.PrintFibonacci();
    }
}
}
