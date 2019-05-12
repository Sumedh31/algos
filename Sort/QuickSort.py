'''
Created on 14-Apr-2019

@author: Sumedh.Tambe
'''
def partition(Arr,low,high):
    i=(low-1)
    pivot=Arr[high]
    for j in range(low,high):
        if(Arr[j]<=pivot):
            i=i+1
            Arr[i],Arr[j] = Arr[j],Arr[i]
    Arr[i+1],Arr[high]=Arr[high],Arr[i+1]
    return(i+1)
def Quicksort(Arr,low,high):
    if(low<high):
        pi=partition(Arr,low,high)
        Quicksort(Arr, low, pi-1)
        Quicksort(Arr, pi+1, high)    

if __name__=="__main__":
    Arr=[10,13,9,5,12,27]
    Quicksort(Arr,0,len(Arr)-1)
    for i in range(len(Arr)):
        print("%d" %Arr[i])
              