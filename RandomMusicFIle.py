'''
Created on 11-Apr-2019

@author: Sumedh.Tambe
'''
import random

if __name__=='__main__':
    Music=[1,2,3,4]
    for I in range(len(Music)):
        number=random.randint(0,len(Music)-1)
        Music[I],Music[number]=Music[number],Music[I]
        
        
    print(Music)