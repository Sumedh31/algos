'''
Created on 07-Aug-2019

@author: Sumedh.Tambe
/ Given a non-empty array of integers, every element appears twice except for one. Find that single one.

//Example 1:

//Input: [2,2,1]
//Output: 1

//Example 2:

//Input: [4,1,2,1,2]
//Output: 4
'''
if __name__=='__main__':
    #givenArr=[4,1,2,1,2]
    givenArr=[-1,0,-1,1,1]
    
    records={}
    for elements in givenArr:
        if elements in records.keys():
            records[elements]+=1
        else:
            records[elements]=1
    for keys in records.keys():
        if records[keys]==1:
            print(keys)