'''
Created on 10-Apr-2019

@author: Sumedh.Tambe
'''
if __name__ == '__main__':
    
    a=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
    EndRowIndex=len(a)
    EndColumnIndex=len(a[0])
    StartingRowIndex=0
    StartingColumnIndex=0
    
    while(StartingRowIndex<EndRowIndex and StartingColumnIndex<EndColumnIndex):
    
        for i in range(StartingColumnIndex,EndColumnIndex):
            print(a[StartingRowIndex][i])
        StartingRowIndex+=1
        
        for i in range(StartingRowIndex,EndRowIndex):
            print(a[i][EndColumnIndex-1])            
        EndColumnIndex-=1
        
        if(StartingRowIndex<EndRowIndex):            
            for i in range(EndColumnIndex-1,StartingColumnIndex-1,-1):
                print(a[EndRowIndex-1][i])
            EndRowIndex-=1
        
        if(StartingColumnIndex<EndColumnIndex):
            for i in range(EndRowIndex-1,StartingRowIndex-1,-1):
                print(a[i][StartingColumnIndex])
            StartingColumnIndex+=1
        
        
        
        
        
    