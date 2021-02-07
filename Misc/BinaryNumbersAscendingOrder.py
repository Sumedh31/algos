'''
Created on 17-Jan-2021

@author: sumedh
Given an array of positive integers, sort the array in ascending order of count of 1s in binary 
representations of array elements. For integers having the same number 1s in their binary representation, 
sort them in ascending order of their integer position E.g the input array is {1,2,3}, then the output array should also be {1,2,3}. Note that both 2 and 3 have the same number of 1 bits.
E.g for [1,3,5,7,8,9] -->['0001', '0011', '0101', '0111', '1000', '1001']

sort the binary as their 1s representation

[['0001','1000'], ['0011','0101','1001'],['0111']]
[[1,8],[3,5,9],[7]]

[0011,0101] will be sorted as [0011,0101] cause their original values will be ordered in ascending order as 3,5 --> [0011,0101]
Output 1,8,3,5,9,7
'''
str1="135789"
list1=[int(a) for a in str1]

binaryPresent=['{0:04b}'.format(element) for element in list1]
print(binaryPresent)
print('{0:04b}'.format(10**5))
