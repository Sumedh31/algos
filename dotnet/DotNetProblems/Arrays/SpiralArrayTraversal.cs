//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.Arrays
//{
//    class SpiralArrayTraversal
//    {
//        static void SpiralTraverse(int [,] arr1,int rows,int cloumn)
//        {
//            int startindexrow = 0;
//            int startindexcol = 0;
//            int endindexrow = rows;
//            int endindexcol = arr1.GetLength(0);
//            while (startindexrow < endindexrow && startindexcol < endindexcol)
//            {

//                for (int i = startindexcol; i < endindexcol; i++)
//                {
//                    Console.Write(arr1[startindexrow, i]+"\n");
//                }
//                startindexrow++;
//                for (int i = startindexrow; i < endindexrow; i++)
//                {
//                    Console.Write(arr1[i,endindexcol-1]+"\n");
//                }
//                endindexcol--;
//                if (startindexrow < endindexrow)
//                {
//                    for (int i = endindexcol-1; i >= startindexcol; i--)
//                    {
//                        Console.Write(arr1[endindexrow-1,i]+"\n");
//                    }
//                }
//                endindexrow--;
//                if (startindexcol < endindexcol)
//                {
//                    for (int i = endindexrow-1; i >= startindexrow; i--)
//                        Console.Write(arr1[i,startindexcol]+"\n");
//                }
//                startindexcol++;
//            }
//        }
//        static void Main(String[] args)
//        {
//            int[,] multiDimensionalArray = new int [4,4]{
//                                           { 1, 2, 3, 4 }, 
//                                           { 5, 6, 7, 8 },
//                                           { 9, 10, 11, 12},
//                                           { 13, 14, 15, 16} 
//                                           };
//            int rows = 4;
//            int column = 4;
//            SpiralTraverse(multiDimensionalArray, rows, column);
//            Console.Read();
//        }
//    }
//}
