//using System;
//using System.Collections.Generic;
//using System.Collections;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.Sorting
//{
//    class MergeSort
//    {
//        static List<int> mergeSortResult(List<int> arr)
//        {
//            if (arr.Count > 1)
//            {
//                int len = arr.Count;
//                int min = 0;
//                int max = len - 1;
//                int mid = (min + len) / 2;

//                List<int> arr1 = new List<int>();
//                List<int> arr2 = new List<int>();

//                for (int i = 0; i < mid; i++)
//                {
//                    arr1.Add(arr[i]);
//                }
//                for (int i = mid; i <= max; i++)
//                {
//                    arr2.Add(arr[i]);
//                }
//                mergeSortResult(arr1);
//                mergeSortResult(arr2);

//                int l, m, n;
//                l = m = n = 0;
//                while (l < arr1.Count && m < arr2.Count)
//                {
//                    if (arr1[l] <= arr2[m])
//                    {
//                        arr[n] = arr1[l];
//                        l += 1;
//                    }
//                    else
//                    {
//                        arr[n] = arr2[m];
//                        m += 1;
//                    }
//                    n += 1;
//                }
//                while (l < arr1.Count)
//                {
//                    arr[n] = arr1[l];
//                    l += 1;
//                    n += 1;
//                }
//                while (m < arr2.Count)
//                {
//                    arr[n] = arr2[m];
//                    m += 1;
//                    n += 1;
//                }
                
//            }
//            return arr;
           
//        }
//        static void Main(String[] args)
//        {
//            List<int> arr = new List<int> { 1, 3, 7, 3, 76, 34, 23, 45 };

//            List<int> result = mergeSortResult(arr);            
//            foreach (int element in result)
//            {
//                Console.Write(element+"\n");
//            }
//            Console.Read();
//        }
//    }
//}
