'''
Created on 11-Jun-2019

@author: Sumedh.Tambe
'''
input_str = "ArtiCStIcs"
#output = "BsujDTuJdt"
output=''
for char in input_str:
    if(ord(char)==90):        
        output+=output.join(chr(65))
    elif(ord(char)==122):
        output+=output.join(chr(97))
    else:
        asciivalue=ord(char)
        output+=output.join(chr(asciivalue+1))

print(output)