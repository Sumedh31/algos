'''
Created on 30-Apr-2019

@author: Sumedh.Tambe Print pyramid pattern
'''

NRows=5
space=8
for I in range(5):
    for J in range(0,space):
        print(end=" ")
            
    for star in range(0,I+1):
        print("P ",end="")
    print("")
    space=space-1
