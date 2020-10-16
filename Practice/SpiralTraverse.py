'''
Created on 23-Jun-2019

@author: Sumedh.Tambe
'''

if __name__=='__main__':
    a=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
    
    startrowindex=0
    endrowindex=len(a)
    startcolumnindex=0
    endcolumnindex=len(a[0])
    
    while(startrowindex<endrowindex and startcolumnindex<endcolumnindex):
        
        for i in range(startcolumnindex,endcolumnindex):
            print(a[startrowindex][i])
        startrowindex+=1
        for i in range(startrowindex,endrowindex):
            print(a[i][endcolumnindex-1])
        endcolumnindex-=1
        if(startrowindex<endrowindex):
            for i in range(endcolumnindex-1,startcolumnindex-1,-1):
                print(a[endrowindex-1][i])
            endrowindex-=1
        if(startcolumnindex<endcolumnindex):
            for i in range(endrowindex-1,startrowindex-1,-1):
                print(a[i][startcolumnindex])
            startcolumnindex+=1
        
        