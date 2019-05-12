'''
Created on 12-May-2019

@author: Sumedh.Tambe
'''
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