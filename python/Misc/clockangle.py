'''
Created on 14-May-2019
/**
* Given a time of day (hour, minute) - return the angle
* between the hour hand and minute hand of a clock face
* set to that time.
* Ex: 90 == clockAngle(3,0)
*/
function clockAngle(hour:int, minute:int):int { return 0; }ex:
assert clockAngle(3,0) == 90

@author: Sumedh.Tambe
'''
import unittest
def clockAngle(hour,minute):
    minuteAngle=minute*6
    hourAngle=5*hour*6+minute
    
    return -1*(minuteAngle-hourAngle)
def testClockAngle():
    if(180==clockAngle(12, 30)):
        print("test case passed")
def legalInput(hour,minute):
    if(0<=minute<=60):
        if(0<=hour<=12):
            minuteAngle=minute*6
            hourAngle=5*hour*6+minute
            result=-1*(minuteAngle-hourAngle)
            
            
    
    
if __name__ == '__main__':
    
    result=clockAngle(12,30)
    print(result)
    
    