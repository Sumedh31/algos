'''2
8
5 1 2 3 7 8 6 4
8
1 2 5 3 7 8 6 4'''    

cases=int(input())
for case in range(cases):
    noOfInputs=int(input())
    inputList=list(map(int,input().split()))
    swaps=[0]*noOfInputs
    swapped=True
    
    while swapped:
        swapped = False
    
        for i in range(noOfInputs):
            while(i<noOfInputs-1 and inputList[i]>inputList[i+1]):
                swaps[inputList[i]-1]+=1
                inputList[i],inputList[i+1]=inputList[i+1],inputList[i]
                swapped=True
                i+=1
    count=0
    for swap in swaps:
        count+=swap
        if(swap>2):
            print("Too chaotoc")
            break
    else:
        print(count)
        