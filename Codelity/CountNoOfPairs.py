'''
Created on 24-Apr-2019
 
@author: Sumedh.Tambe
'''
#Write a function to count number of pair in array of integers 
#  
# for example:  
# ar = [2,3,4,23,4,3,3] there is one pair of `4` and `3` and there are three with out pair left.
# The function should return 2
#  
# Constrints
# - 0 < |ar| <= 100,000
# - 0 < ar[i] <= 100   
# 
# example1: ar = [2,3,4,23,4,3,3] Output -> 2
# example2: ar = [2,3,4,23,4,3,3,2] Output -> 3
# example3: ar = [1,1,1,1] Output -> 2
#  
def pairCount(ar):
    Dictpair={}
    TotalPair=0
    for I in ar:        
        if I in Dictpair.keys():
            Dictpair[I]=Dictpair[I]+1
            if(Dictpair[I]%2==0):
                TotalPair+=1             
        else:
            Dictpair[I]=1
    return TotalPair
     
     
#     for Items in Dictpair.values(): 
#         Currentpair=0            
#         Currentpair=Items//2 
#         TotalPair+=Currentpair
#     return TotalPair
        
if __name__ == '__main__':    
     
    Arraylist=[1,1,1,1,2,3,2,4]
     
    result=pairCount(Arraylist)
    print(result)