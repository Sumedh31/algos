# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
from dataclasses import dataclass
import re
 
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
#     inputString='my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b\nmy2.song.mp3 1000b'
#     #inputString=input()
#     'my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'
#     result=solution(inputString)
#     print(result)

@dataclass
class Images:
    file_name: [str]
    memory: int

    def size(self, memory_size: int):
        self.memory += memory_size

    def __str__(self):
        filenames = ",".join(self.file_name)
        total_size = self.memory
        return f"Images: {filenames}\n Total Size is: {total_size}"

@dataclass
class Videos:
    file_names: [str]
    size: int
    def size(self, memory: int):
        self.size += memory

    def __str__(self):
        return f"Videos: {','.join(self.file_names)}\n Total Size is: {self.size}"

@dataclass
class Text:
    file_names: [str]
    size: int
    def size(self, memory: int):
        self.size += memory

    def __str__(self):
        return f"Videos: {','.join(self.file_names)}\n Total Size is: {self.size}"


@dataclass
class Other:
    file_names: [str]
    size: int
    def size(self, memory: int):
        self.size += memory

    def __str__(self):
        return f"Videos: {','.join(self.file_names)}\n Total Size is: {self.size}"


def solution(input_string: str):
    music_extension, video_extension, image_extension = ["mp3", "aac", "flac"], ["mp4", "avi", "mkv"], ["jpg", "bmp", "gif"]

def get_file_details(file_details:str):
    file_size =  file_details.split(".")



if __name__ == '__main__':
    inputString = 'my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b\nmy2.song.mp3 1000b'


