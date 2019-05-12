from builtins import breakpoint

Max=256

def comopare(arr1,arr2):
    for i in range(Max):
        if(arr1[i]!=arr2[i]):
            return False    
    return True
def searchit(pat, txt): 
  
    M = len(pat) 
    N = len(txt) 
  
    # countP[]:  Store count of 
    # all characters of pattern 
    # countTW[]: Store count of 
    # current window of text 
    countP = [0]*Max
    countW=[0]*Max  
          
    for i in range(len(pat)): 
        countP[ord(pat[i]) ]+= 1
        countW[ord(txt[i])]+=1
        
    for i in range(len(pat),len(txt)):
        
        if(comopare(countP, countW)):
            print("found at",i-len(pat))
        #get the next element from text and add to the list of 0's
        countW[ord(txt[i])]+=1
        countW[ord(txt[i-len(pat)])]-=1
        
    if (comopare(countP, countW)):
        print("Found at index",len(txt)-len(pat))
        
        
            
        
        
txt = "BACDGABCDA"
pat = "ABCD"       
searchit(pat, txt)    