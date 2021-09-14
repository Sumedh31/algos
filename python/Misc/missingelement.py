'''
Created on 11-Jun-2019

@author: Sumedh.Tambe
'''
input_seq = [1, 2, 3, 4, 5, 7, 8, 9, 10]
#Ans: 6
# Ans: 6
n=len(input_seq)+1

totalSum=(n*(n+1))/2

actualSum=sum(input_seq)

MissingElement=totalSum-actualSum

print(MissingElement)
