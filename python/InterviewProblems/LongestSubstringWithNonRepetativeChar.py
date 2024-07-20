'''
Created on 13-May-2020

@author: Sumedh
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
Brute force
STep1: Get all substrings of given string
Step2: Iterate over each substring and check for allunique characters 
Step3: Store the maxlenghth of substring if it is greater than previous max
'''

class SolutionBruteForce(object):
    def lengthOfLongestSubstringBrute(self,s):        
        longeststring=""
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if(len(s[i:j])>len(longeststring) and self.isAllUnique(s[i:j])):
                    longeststring=s[i:j]
        return len(longeststring)
             
    def isAllUnique(self,chars):
        existingchar=[]        
        for char in chars:
            if not char in existingchar:
                existingchar.append(char)
            else:
                return False
        return True
     
if __name__=='__main__':
    sln=SolutionBruteForce()
    s="abcabcbb"
    lengthg=sln.lengthOfLongestSubstringBrute(s)
    print(lengthg)
''' 
Optimized Solution using window sliding - 1
Step1: Iterate over each character from string and maintain a list of each such character traversed.
Step2: If you have hit the repeated char that is present in list then keep popping the first index character
until the character is no longer present in the list. This will ensure left window of substring is correct.
Step3: Update the max if length of maintainer list exceeds previous max.
'''
class SolutionOptimized1(object):    
    def lengthOfLongestSubstringOptimized1(self,s): 
        maintainer=[]
        ans=0
        for char in s:
            if(char not in maintainer):
                maintainer.append(char)
                if(len(maintainer)>ans):
                    ans=len(maintainer)
            else:
                while(char in maintainer):                
                    maintainer.pop(0)
                maintainer.append(char)
        if(len(maintainer)>ans):
            ans=len(maintainer)
        return ans
  
if __name__=='__main__':
    s=" "
    lengh=SolutionOptimized1().lengthOfLongestSubstringOptimized1(s)
    print(lengh)

''' 
Optimized Solution using window sliding - 2
Step1:Iterate over each character from string and maintain a dictionary of each such character traversed 
      where value is the current index of that character.
Step2: If you have hit the repeated char that is present in dictionary then you need to reset your left open in window sliding approach.
    Step2A- You get the index of repeated char by reading the value of that key.So your new left open index should be the current index of repeated charcter.
            You get that by adding 1 to the previous appeared index of repeated character. and if that is greater than previous leftopen value
            you should update it. This is because we are maintaining all chars in dict hence we need to sure that we are reseting to right left open index.
Step3: Update max with every iteration by substracting leftopen index in every iteration. (-1 because index starts at 0)            
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        maintainer={}
        startresetindex=0
        ans=0
        for i,char in enumerate(s):
            if char in maintainer.keys():
                currentrepeatcharindex=maintainer[char]+1
                if currentrepeatcharindex>startresetindex:
                    startresetindex=currentrepeatcharindex
            num=i-startresetindex+1
            if(num>ans):
                ans=num
            maintainer[char]=i
        return ans
                
        
if __name__=='__main__':
    s="abba"
    lengh=Solution().lengthOfLongestSubstring(s)
    print(lengh)


def long(s):
    long_str =""
    start, end = 0, 0
    char_set = set()
    while end < len(s):
        if s[end] not in char_set:
            char_set.add(s[end])
            end+=1
        else:
            if end -start > len(long_str):
                long_str =  s[start: end]
            char_set.remove(s[start])
            start += 1
    if end - start > len(long_str):
        long_str = s[start:end]
    return long_str

print(f"and is {long('abcabcbb')}")

