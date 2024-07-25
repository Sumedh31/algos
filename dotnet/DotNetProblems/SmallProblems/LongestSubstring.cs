    
    namespace Practicecoding.Misc{
    class LongestSubstringProblem{
        public static string LongestSubString(string input){
            string longestSubString="";
            for(int i = 0; i<input.Length;i++){
                for(int j = i+1;j<input.Length;j++){
                   if(input[i..j].Length > longestSubString.Length && AreAllUnique(input[i..j])){
                    longestSubString = input.Substring(i,j);
                   }
                }
            }
            return longestSubString;
        }

        public static bool AreAllUnique(string str){
            List<char> existing = new List<char>();
            foreach(char chr in str){
                if(existing.Contains(chr)){
                    return false;
                }
                else{
                    existing.Add(chr);
                }
            }
            return true;

        }

        public static void Main(String[] args) {
            Console.WriteLine("Here is  " + LongestSubString("abcabcbb"));
        }  
    }
}
