from typing import List,Any,Optional
class Node:
    def __init__(self,data: Any,next: Optional = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f"Node({self.data})"
class Linkedqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    # 进队
    def put(self,data: Any):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    # 出队
    def pop(self):
        if self.front is None:
            raise IndexError("空队列")
        else:
            node = self.front
            self.front = self.front.next
            self.size -= 1
    # 取值
    def get(self,index: int):
        if index < 0 or index >= self.size:
            raise Exception("越界")
        cur = self.front
        for _ in range(index):
            cur = cur.next
        return cur
    # 是否为空
    def is_empty(self):
        return self.front is None
    def __repr__(self):
        cur = self.front
        result = ""
        while cur is not None:
            result += f"{cur}<--"
            cur = cur.next
        return result + "End"
if __name__ == '__main__':
    q = Linkedqueue()
    q.put(1)
    q.put(58)
    q.put(66)
    q.put(24)
    print(q)
    q.pop()
    print(q)
    print(q.get(0))
    print(q.get(1))
    print(q.get(2))







