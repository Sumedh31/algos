using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetProblems.DataStructures
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val)
        {
            this.val = val;
            this.next = null;
        }
    }
    public class LinkedList
    {
        ListNode head;
        ListNode tail;

        public ListNode GetLinkedList(int[] arr1)
        {
            foreach (int item in arr1)
            {
                ListNode referNode = new ListNode(item);
                InsertNode(referNode);
            }
            return head;
        }
        public void InsertNode(ListNode element)
        {
            if (tail != null)
                tail.next = element;
            element.next = null;
            tail = element;
            if (head == null)
                head = tail;
        }
    }
    public static class AddTwoNumbersUsingLinkiedList
    {
        public static void Init()
        {
            int[] arr1 = { 1,2,3};
            int[] arr2 = { 4, 5, 6 };
            LinkedList tempobj = new LinkedList();
            LinkedList tempobj2 = new LinkedList();
            ListNode arr1Head = tempobj.GetLinkedList(arr1);
            ListNode arr2Head = tempobj2.GetLinkedList(arr2);
            AddTwoNumbers(arr1Head, arr2Head);
        }        
        public static ListNode AddTwoNumbers(ListNode l1,ListNode l2)
        {
            ListNode dummyhead = new ListNode(0);
            ListNode current = dummyhead;
            ListNode curfirsthead = l1;
            ListNode cursecondhead = l2;
            int carry = 0;
            int sum = 0;
            while(curfirsthead!=null || cursecondhead!=null)
            {
                var x = curfirsthead != null ? curfirsthead.val : 0;
                var y = cursecondhead != null ? cursecondhead.val : 0;
                sum = x + y+ carry;
                carry = sum / 10;
                current.next = new ListNode(sum%10);
                current = current.next;
                if(curfirsthead!=null)
                {
                    curfirsthead = curfirsthead.next;
                }
                if(cursecondhead!=null)
                {
                    cursecondhead = cursecondhead.next;
                }               

            }
            if (carry > 0)
            {
                current.next = new ListNode(carry);
            }
            return dummyhead.next;
        }
        
    }
}
