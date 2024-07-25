//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

namespace DotNetProblems.SmallProblems
{
    class PrintPyramidClass{
        public static void PrintPyramid(int lines){
            int spaces = lines + 3;
            for(int i =0;i < lines;i++){
                for(int j=0; j< spaces; j++){
                    Console.Write(" ");
                }

                for(int k=0; k<=i; k++){
                    Console.Write("P ");
                }
                Console.WriteLine("");
                spaces-=1;
            }


        }

        public static void Main(){

            PrintPyramid(5);
        }
    }

}
