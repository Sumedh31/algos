'''
Created on 13-Oct-2020

@author: Sumedh
'''

#!/bin/python3

import os
import sys
import types

#
# Complete the 'cmap' function below.
#
# The function is expected to return a generator (instance of `types.GeneratorType`).
# The function accepts following parameters:
#  1. list of functions (lambda x: ...)
#  2. list of integers

# 
# def cmap(funcs, arr):
#     # Write your code here
#     updatedValue=arr
#     for func in funcs:
#         for I in range(len(updatedValue)): 
#             updatedValue[I]=func(updatedValue[I])
#     for values in updatedValue:                   
#         yield values
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# 
#     funcs_count = int(input().strip())
# 
#     funcs = []
# 
#     for _ in range(funcs_count):
#         funcs_item = input().strip()
#         funcs.append(eval(funcs_item))
# 
#     arr_count = int(input().strip())
# 
#     arr = []
# 
#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)
# 
#     result = cmap(funcs, arr)
#     assert(isinstance(result, types.GeneratorType))
#     output = []
#     for result_item in result:
#         output.append(result_item)
#     fptr.write('\n'.join(map(str, output)))
#     fptr.write('\n')
# 
#     fptr.close()


def cmap(funcs, arr):
    # Write your code here
    updatedValue=arr
    for I in range(len(updatedValue)):
        #ele=updatedValue[I] 
        for func in funcs:
            arr[I]=func(arr[I])
        yield arr[I]
funcs=[lambda x:x*x,lambda x:x+x]
arr=[1,2,3,4]
value=cmap(funcs,arr)
lus=[]
for val in value:
    lus.append(val)
print (lus)
    
