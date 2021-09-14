'''
Created on 14-Apr-2019

@author: Sumedh.Tambe
'''

def MergeSort(arr):
    
    if(len(arr)>1):
        mid=len(arr)//2
        A=arr[:mid]
        B=arr[mid:]
        MergeSort(A)
        MergeSort(B)
        i=j=k=0
        while(i<len(A) and j<len(B)):
            if(A[i]<=B[j]):
                arr[k]=A[i]
                i+=1
            else:
                arr[k]=B[j]
                j+=1
            k+=1
        while(i<len(A)):
            arr[k]=A[i]
            i+=1
            k+=1
        while(j<len(B)):
            arr[k]=B[j]
            j+=1
            k+=1
    return arr
if __name__ == '__main__':
    array=[1,3,7,3,76,34,23,45]
    #array=[2, 5, 4, 3, 7, 9, 1, 6]
      
    result=MergeSort(array)
    print(result)
    
        
    