# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# 
# #import re
# 
# def getExtension(fileName):
#     file=fileName.split(".")
#     extension=file[len(file)-1]
#     return extension
#     
# def solution(S):
#     # write your code in Python 3.6
#     finalString=S.split("\n")
#     #finalString=re.split('/\n|\\\\',S)
#     typeOfFiles={"music":0,"images":0,"movies":0,"other":0}
#     
#     for element in finalString:
#         fileDetails=element.split(" ")
#         fileName=fileDetails[0]
#         fileSize=fileDetails[1].split("b")
#         
#         fileExtension=getExtension(fileName)
#         if(fileExtension=="mp3" or fileExtension=="aac" or fileExtension=="flac" ):
#             typeOfFiles["music"]+=int(fileSize[0])
#         elif(fileExtension=="jpg" or fileExtension=="bmp" or fileExtension=="gif"):
#             typeOfFiles["images"]+=int(fileSize[0])
#         elif(fileExtension=="mp4" or fileExtension=="avi" or fileExtension=="mkv"):
#             typeOfFiles["movies"]+=int(fileSize[0])
#         else:
#             typeOfFiles["other"]+=int(fileSize[0])
#             
#     mystring=""
#     
#     for key,value in typeOfFiles.items():
#         mystring=mystring+key+" "+str(value)+"b"+"\n"
#                
#     return mystring
# 
# if __name__ == '__main__':
#     
#     inputString=input()
#     'my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'
#     result=solution(inputString)
#     print(result)
        
if __name__ == '__main__':
    ans = 0
    A=[10,23,45]
    for i in range(0, len(A)):
        if A[i] < ans:
            ans = A[i]
    
    