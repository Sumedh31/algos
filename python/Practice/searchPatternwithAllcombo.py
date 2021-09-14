'''
Created on 23-Apr-2020

@author: Sumedh
'''
txt = "BACDGABCDA"
pat = "ABCD"       

def getweight(str):
    weight=0
    for char in str:
        weight+=ord(char)
    return weight
def searchPattern(text,pattern):
    patternweight=getweight(pattern)
    end=len(pattern)
    for i in range(0,len(text)-len(pattern)+1):        
        checkstring=text[i:end]
        if(getweight(checkstring)==patternweight):
            print("pattern present at index", i) 
        end+=1       
if __name__=='__main__':
    searchPattern(txt, pat)
        
        