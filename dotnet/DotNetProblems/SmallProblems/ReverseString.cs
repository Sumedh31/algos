    
    namespace Practicecoding.Misc{
    class ReverseString{
        public static string ReverseAString(string input){
            string reveresed = "";
            for(int i = input.Length - 1; i >=0; i--){
                reveresed += input[i];
            }
            return reveresed;

        }

        public static void Main(String[] args) {
            Console.WriteLine("Here is  " + ReverseAString("hello"));
        }  
    }
}
