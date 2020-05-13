'''
Created on 13-May-2020

@author: Sumedh
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
'''

class solution(object):
    def lengthOfLongestSubstring(self,s):
        substrings=self.getAllSubstrings(s)
        longeststring=""
        for currentstring in substrings:
            if(len(currentstring)>len(longeststring)):
                chararr=[char for char in currentstring]
                if(self.isAllUnique(chararr)):
                    longeststring=currentstring
        print(longeststring)
            
    def getAllSubstrings(self,s):
        n=len(s)
        subs=[]
        for i in range(n):
            for j in range(i+1,n+1):
                subs.append(s[i:j])
        print(subs)
        return subs
    def isAllUnique(self,chars):
        existingchar=[]
        
        for char in chars:
            if not char in existingchar:
                existingchar.append(char)
            else:
                return False
        return True
                            
    
if __name__=='__main__':
    sln=solution()
    s="abcabcbb"
    sln.lengthOfLongestSubstring(s)
