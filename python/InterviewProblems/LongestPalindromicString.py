"""
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Steps for string baddad
1: Expand range around b and ba
2: Expand range around a and ad
3: Expand range around d and dd
4: Expand range around d and da
5: Expand range around a and ad
6: Expand range around d and endofstring now
The expand range function would iterate as long as
The beginning index is > 0 (we will expand begin index to left hence we need to decrease the startindex)
The end index is < len(s)
and until we are getting similar character around the center that is s[begin]==s[end]
Once the loop is broken we return the length of max palindrome (it could also be length of palindrome with one char or 2
char at center)

"""

def longestPalindrome(s: str) -> str:
    result_start = 0
    result_length = 0
    for i in range(len(s)):
        # Check expansion beginning at the first i th char
        start = i
        end =i
        # Get the max length of palindrome considering only one character as center one_char_center[0] = max_length
        # of 1 char center palindrome
        one_char_center = expandFromCenter(s, start, end)
        # Get the max length of palindrome considering two character at center
        two_char_center = expandFromCenter(s, start, end+1)
        # The req max result_length would be the maximum of len1 and len2 because the biggest
        # palindrome could be around 1 char or 2 char
        max_length = max(one_char_center[0], two_char_center[0])
        if result_length < max_length:
            result_length = max_length
            # if len1[0] that is the max length around is max length get the begin value from len1
            if max_length == one_char_center[0]:
                result_start = one_char_center[1]
            else:
                result_start = two_char_center[1]
    return s[result_start:result_length+result_start]


def expandFromCenter( s, start_index:int, end_index:int):
    while start_index >= 0 and end_index < len(s) and s[start_index] == s[end_index]:
        start_index -= 1
        end_index += 1
    max_length = end_index - start_index - 1
    # Return start_index+1 because we have already decreased it once before breaking from the loop
    return max_length, start_index+1


print(longestPalindrome('baddad'))
print(longestPalindrome('babb'))
print(longestPalindrome('baba'))
def longest_palindrome(s):
    long_pal = ""
    for i in range(len(s)):
        # find odd length palindrome
        left, right = i, i
        while left > 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(long_pal) < right - (left+1):
            long_pal = s[left+1: right]

        # find even length palindrome
        left, right = i, i+1
        while left > 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(long_pal) < right - (left+1):
            long_pal = s[left+1: right]
    return long_pal

print(longest_palindrome('baddad'))



