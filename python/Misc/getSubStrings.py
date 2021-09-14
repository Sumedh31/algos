'''
Created on 12-Jul-2019

@author: Sumedh.Tambe
'''
def substrings(s,n):
    for i in range(n):
        for len in range(i+1,n+1):
            print(s[i:len])

if __name__=='__main__':
    str1='abcd'
    print(len(str1))
    print(str1[0:4])
    substrings(str1, len(str1))