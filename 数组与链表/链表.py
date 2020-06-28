# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return f"Node({self.data})"
#
# class LinkList:
#     def __init__(self):
#         self.head = None
# 插入头节点
#     def insert_head(self,data):
#         new_node = Node(data)
#         if self.head is not None:
#             new_node.next = self.head
#         self.head = new_node
#
#     def print_list(self): #只打印链表里的值
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next
#
#     def __repr__(self): #打印链表本身
#         cur = self.head
#         result = ""
#         while cur is not None:
#             result += f"{cur}-->"
#             cur = cur.next
#         return result + "END"
# if __name__ == '__main__':
#     test = LinkList()
#     test.insert_head(100)
#     test.insert_head(200)
#     test.insert_head(300)
#     print(test)
#     print("----------------")
#     test.print_list()


from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):  #重写方法
        return f"Node({self.data})"
# if __name__ == '__main__':
#     n = Node(5)
#     print(n)
class Linklist:
    def __init__(self):
        self.head = None
    #插入头节点
    def insert_head(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
    #插入尾节点
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)
    #中间插入节点
    def insert(self,i,data):
        if i == 1 or self.head is None:
            self.insert_head(data)
        else:
            curr = self.head
            prev = self.head
            new_node = Node(data)
            j = 1
            while j < i:
                prev = curr
                curr = curr.next
                j += 1
            prev.next = new_node
            new_node.next = curr

    # 用列表构建链表
    def Linklist(self,obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next
    #删除头部
    def delete_head(self):
        if self.head is None:
            print("这是一个空链表")
        else:
            self.head = self.head.next

    #删除尾部
    def pop(self):
        curr = self.head
        if curr is  None:
            print("这是一个空链表")
        else:
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            curr.next = None
            return temp
    def delete_tail(self):
        curr = self.head
        if curr is None:
            print("这是一个空链表")
        else:
            curr = self.head
            prev = curr
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None

    # 只打印链表里的值
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # 打印链表本身
    def __repr__(self):
        current = self.head
        string_re = ""
        while current is not None:
            string_re += f"{current}-->"
            current = current.next
        return string_re + "end"

if __name__ == '__main__':
    a = Linklist()
    a.insert_head(10)
    a.insert_head(30)
    a.append(10000)
    a.append(20000)
    a.insert(3,500)
    # a.Linklist([1,23,42,55,66])
    # a.delete_tail()
    print(a)
    print("------------")
    a.print_list()





