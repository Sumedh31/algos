using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicecoding.Misc
{
    class Anagram
    {
    // public static bool AreAnagrams(string firstWord, string secondWord)
    // {
    //     char [] firstWordArray = firstWord.ToCharArray();
    //     char [] secondWordArray = secondWord.ToCharArray();

    //     Array.Sort(firstWordArray);
    //     Array.Sort(secondWordArray);

    //     return new string(firstWordArray) == new string(secondWordArray);    
    // }

    public static bool AreAnagrams(string firstWord, string secondWord){
        Dictionary<char, int> firstWordCharCount = GetCharacterCount(firstWord);
        Dictionary<char, int> secondWordCharCount = GetCharacterCount(secondWord);

        if (firstWordCharCount.Count != secondWordCharCount.Count){
            return false;
        }

        else{
            foreach(var kvp in firstWordCharCount){
                if(!secondWordCharCount.ContainsKey(kvp.Key) || secondWordCharCount[kvp.Key] != kvp.Value){
                    return false;
                }
            }
            return true;
        }
    }

    public static Dictionary<char, int> GetCharacterCount(string word){
        Dictionary<char, int> characterCount = [];

        foreach(char chr in word.ToCharArray()){
            if (characterCount.ContainsKey(chr)){
                characterCount[chr] += 1;
            }
            else{
                characterCount[chr] = 1;            }
        }
        return characterCount;
    }

    public static void Init()
    {
          Console.WriteLine(AreAnagrams("listen", "silent"));
          Console.WriteLine(AreAnagrams("hello", "world"));   
    }
}
