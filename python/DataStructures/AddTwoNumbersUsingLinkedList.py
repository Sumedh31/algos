'''
Created on 20-May-2020

@author: Sumedh
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Use LinkedList
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
from test.test_shelve import L1

class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= None
class LinkedList():
    def __init__(self):
        self.head=ListNode(None) 
        self.tail=ListNode(None)   
    def GetHead(self,list1):
        for values in list1:
            referNode=ListNode(values)
            self.InsertNode(referNode)
        return self.head
    def InsertNode(self,ListNode):
        if self.tail.val !=None:
            self.tail.next=ListNode
#         ListNode.prev=self.tail
        ListNode.next=None
        self.tail=ListNode
        if self.head.val==None:
            self.head=self.tail
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry,sum=0,0
        dummyhead=ListNode()
        current=dummyhead
        l3=ListNode()
        p=l1
        q=l2
        while(p!=None or q!=None):
            x=p.val if p!=None else 0
            y=q.val if q!=None else 0
            sum=x+y+carry
            carry=sum//10
            current.next=ListNode(sum%10)
            current=current.next
            p=p.next if p!=None else None
            q=q.next if q!=None else None
        if(carry>0):
            current.next=ListNode(carry)
        while(dummyhead):
            print(dummyhead.val)
            dummyhead=dummyhead.next
        return dummyhead.next
            
if __name__=='__main__':
    list1=[1,2,3]
    list2=[4,5,6]
    linkedlistobj=LinkedList()
    linkedlistobj2=LinkedList()
    l1=linkedlistobj.GetHead(list1)
    l2=linkedlistobj2.GetHead(list2)
    sln1=Solution()
    sln1.addTwoNumbers(l1, l2)
    
        
    
        
