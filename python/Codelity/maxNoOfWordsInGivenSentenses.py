'''
Created on 12-May-2019

@author: Sumedh.Tambe
'''
#  import re
#  
#  print(re.split('\.|\?|!',"We test coders. Give us a try?"))#   
#  res = len("We test coders".split())
#  print(res)
# COunt no of max words from given a string of sentenses.
import re
def solution(S):
    # write your code in Python 3.6
    ListOfSentense=re.split('\.|\?|!',S)
    MaxWordsInSentense=0
     
    for TestString in ListOfSentense:
        Words = len(TestString.split())
        if(Words>MaxWordsInSentense):
            MaxWordsInSentense=Words
    return MaxWordsInSentense
         
     
     
if __name__ == '__main__':
    InputString="Forget  CVs..Save time . x x. mY nAME IS THIS REALLY! AND WHATS YOUR'S pLEASE TELL ME?"
    print(solution(InputString))