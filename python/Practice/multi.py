'''
Created on 14-Apr-2020

@author: Sumedh
def getData():
    
    try:
        while True:
            data=input()
            if not data:
                yield from data
            else:
                yield data
        except KeyboardInterrupt:
        return
'''
from _ast import Try
def f(flag):
    n = 10
    if flag:
        for i in range(n):
            yield i
    else:
        yield from range(n)
        
    
if __name__ == '__main__':
    CallLogs = f(True)
        
    print(CallLogs)