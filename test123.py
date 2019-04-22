# '''
# Created on 12-Apr-2019
# 
# @author: Sumedh.Tambe
# '''
# A = [ 100, 3, 1]
# n=len(A)
# leng=0
# cnt=0
# for i in range (n - 1) : 
#           
#         # If arr[i+1] is less than arr[i], 
#         # then increment length 
#     if (A[i + 1] < A[i]): 
#             leng+=1
#     else:
#         cnt+=(((leng-1)*leng//2))
#     if(leng>1):
#         cnt+=(((leng-1)*leng//2))
#         
# print(cnt)
x=0
print(sum(x+numbers for numbers in range(10) if numbers%2==0))