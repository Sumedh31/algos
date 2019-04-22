#  import re
#  
#  print(re.split('\.|\?|!',"We test coders. Give us a try?"))
#  
#  res = len("We test coders".split())
#  print(res)
# 
# import re
# def solution(S):
#      write your code in Python 3.6
#     ListOfSentense=re.split('\.|\?|!',S)
#     MaxWordsInSentense=0
#     
#     for TestString in ListOfSentense:
#         Words = len(TestString.split())
#         if(Words>MaxWordsInSentense):
#             MaxWordsInSentense=Words
#     return MaxWordsInSentense
#         
#     
#     
# if __name__ == '__main__':
#     InputString="Forget  CVs..Save time . x x. mY nAME IS THIS REALLY! AND WHATS YOUR'S pLEASE TELL ME?"
#     print(solution(InputString))
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A, B):
#     # write your code in Python 3.6
#     ListOfDigitsInA=[int(d) for d in str(A)]
#     ListOfDigitsInB=[int(d) for d in str(B)]
#     DecimalZip=[]
#     
#     if(len(ListOfDigitsInA)>=len(ListOfDigitsInB)):
#         Max=len(ListOfDigitsInA)
#     else:
#         Max=len(ListOfDigitsInB)
#     
#     for I in range(Max):
#         if(len(ListOfDigitsInA)>I):            
#             DecimalZip.append(ListOfDigitsInA[I])
#         if(len(ListOfDigitsInB)>I):
#             DecimalZip.append(ListOfDigitsInB[I])
#     
#     DecimalZipNumber=''.join(str(x) for x in DecimalZip)
#     
#     if(int(DecimalZipNumber)>=100000000):
#         return -1
#     else:
#         return int(DecimalZipNumber)
#         
# if __name__ == '__main__':
#     A=123000
#     B=0
#     print(solution(A,B))
#   

def solution(CallLogs):
    # write your code in Python 3.6
    for I in range(len(CallLogs)):
        Duration=CallLogs[I][0]
        Number=CallLogs[I][1]
    

def multi_input():
    try:
        while True:
            data=input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return
    
if __name__ == '__main__':
    CallLogs = list(multi_input())
    FirstEle=CallLogs[0].split(',')
    print(FirstEle)
    