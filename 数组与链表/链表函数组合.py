from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self,index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    def insert(self,index,element):
        new_node = Node(element)
        if index < 0 or index > self.size:
            raise Exception("数组越界")
        elif self.size == 0: #空链表
            self.head = new_node
            self.tail = new_node
        elif index == 0:     #插入头节点
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:   #插入尾节点
            self.tail.next = new_node
            self.tail = new_node
        else:
            pre = self.get(index-1)
            new_node.next = pre.next
            pre.next = new_node
        self.size += 1
    def remove(self,index):
        if index < 0 or index > self.size:
            raise Exception("数组越界")
        if index == 0 :
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size:
            pre = self.get(index-1)
            remove_node = pre.next
            self.tail = pre
            pre.next = None
        else:
            pre = self.get(index-1)
            remove_node = pre.next
            pre.next = pre.next.next
        self.size -= 1
    def reverse(self):
        pre = None
        cur = self.head
        while cur is not None:
            temp = cur.next
            if pre is None:
                cur.next = pre
            else:
                cur.next = pre
            pre = cur
            cur = temp
        self.head = pre

    def __repr__(self):
        cur = self.head
        result = ""
        while cur is not None:
            result += f"{cur}-->"
            cur = cur.next
        return result + "End"
if __name__ == '__main__':
    a = Linklist()
    a.insert(0,100)
    a.insert(1,200)
    a.insert(2,300)
    a.insert(2,800)
    a.insert(1,99)
    print(a)
    # a.get(1)
    a.reverse()
    print(a)
