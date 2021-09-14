using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetProblems.DataStructures
{
    class LRUUsingLinkedList
    {
        public static void Init()
        {
            LRUCache cache = new LRUCache(2);
            cache.put(1);
            cache.put(2);
            cache.put(3);
            cache.put(2);
            Console.WriteLine(cache.get(2));
            Console.WriteLine(cache.get(1));
            Console.Read();
        }
    }
    class Node
    {
        public int key;
        public int value;
        public Node prev;
        public Node next;
        public Node(int key,int value)
        {
            this.key = key;
            this.value = value;
        }
    }
    class LRUCache
    {
        Node head;
        Node tail;
        int capacity;
        Dictionary<int, Node> map;
        public LRUCache(int capacity)
        {
            this.capacity = capacity;
            this.map = new Dictionary<int, Node>();
        }
        
        public int get(int key)
        {
            if (!map.ContainsKey(key))
            {
                return -1;
            }
            else
            {
                Node referNode = map[key];
                RemoveNode(referNode);
                InsertNode(referNode);
                return referNode.value;
            }
        }
        public void put(int key)
        {
            if (map.ContainsKey(key))
            {
                Node referNode = map[key];
                RemoveNode(referNode);
                InsertNode(referNode);
            }
            else
            {
                if(map.Count>=capacity)
                {
                    map.Remove(head.key);
                    RemoveNode(head);
                }
                Node referNode = new Node(key, key);
                InsertNode(referNode);
                map.Add(key, referNode);
            }
        }
        public void InsertNode(Node node)
        {
            if(tail!=null)
            {
                tail.next = node;
            }
            node.prev = tail;
            node.next = null;
            tail = node;
            if (head == null)
            {
                head = tail;
            }
        }
        public void RemoveNode(Node node)
        {
            if(node.prev==null)
            {
                head = node.next;
            }
            else
            {
                node.prev.next = node.next;
            }
            if(node.next==null)
            {
                tail = node.prev;
            }
            else
            {
                node.next.prev = node.prev;
            }
        }
    }

}
