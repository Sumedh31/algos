//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace DotNetProblems.Dictionaries
//{
//    class LRUUsingDict
//    {
//        static Dictionary<int,int> Access(int cache)
//        {
//            Dictionary<int,int> lru=new Dictionary<int,int>();
//            Dictionary<int, int> sortedLRU = new Dictionary<int, int>();
//            if(lru.ContainsKey(cache))
//            {
//                lru[cache] += 1;
//            }
//            else
//            {
//                if (lru.Count >= 5)
//                {
//                    foreach (KeyValuePair<int, int> caches in lru.OrderBy(key => key.Value))
//                        sortedLRU.Add(caches.Key, caches.Value);
//                    lru.Clear();
//                    lru = sortedLRU;
//                    lru.Remove(lru.Keys.Last());
//                }
//                else
//                {
//                    lru.Add(cache, 1);
//                }
//            }
//            return lru;

//        }
//        static void Main()
//        {
//            Access(20);
//        }
//    }
//}
