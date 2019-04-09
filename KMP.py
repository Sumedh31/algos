'''
Created on 06-Apr-2019

@author: Sumedh.Tambe
'''
def KMPSearch(pat,txt):
    lps=[0]*len(pat)
    j=0 #Pattern index
    
    computeLPSArr(pat,len(pat),lps)
    
    
def computeLPSArr(pat,lenofpat,lps):
    length=0
    i=1
    
    while i<lenofpat:
        if pat[i]==pat[length]:
            length+=1
            lps[i]=length
            i+=1
            
            
        
    
    
    
    
    

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat,txt)