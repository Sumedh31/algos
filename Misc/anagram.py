'''
Created on 20-May-2019

@author: Sumedh.Tambe
'''

def checkAnagaram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
    


if __name__ == '__main__':
    str1="AARMY"
    str2="MARYY"
    
    result=checkAnagaram(str1,str2)
    print(result)