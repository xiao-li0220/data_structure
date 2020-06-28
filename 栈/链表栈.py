from typing import Any,Optional,NoReturn
class Node:
    def __init__(self,data: Any,next: Optional==None):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class Linkedstack:
    def __init__(self):
        self.top = None

    # 压栈
    def push(self,data) -> NoReturn:
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
    # 弹栈
    def pop(self):
        if self.top is None:
            raise  IndexError("这是一个空栈")
        else:
            new_node = self.top
            self.top = new_node.next
            self.size -= 1
            return new_node.data
    def is_empty(self):
        return self.top is None
    def peek(self):
        if self.top is not None:
            return self.top
    def length(self):
        return self.size
    def __repr__(self):
        cur = self.top
        result = ""
        while cur is not None:
            result += f"{cur}-->"
            cur = cur.next
        return result + "End"
if __name__ == '__main__':
    a = Linkedstack()
    a.push(1)
    a.push(2)
    a.push(6)
    a.push(55)
    print(a)
    a.pop()
    print(a)
    print(a.peek())
    print(a.is_empty())
    print(a.length())