using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicecoding.Misc
{
    class GetSubstrings
    {
        public static void GetSubStrings(string str){
            for(int i =0; i< str.Length; i++) {
                for(int j=i; j<str.Length; j++){
                    Console.WriteLine("Substring "+str.Substring(i,j-i+1));
                    char[] arr = str.Substring(i,j-i+1).ToCharArray();
                    Array.Reverse(arr);
                    if(!str.Substring(i,j-i+1).Equals(new string(arr))){
                        Console.WriteLine("Substring "+new string(arr));
                    }
                    
                }
            }
        }

        public static void Main(){

            GetSubStrings("ABC");
        }
    }
}
