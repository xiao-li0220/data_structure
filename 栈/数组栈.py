class Stack:
    def __init__(self,limit):
        self.stack = []
        self.size = 0
    def __str__(self):
        return str(self.stack)
# 压栈
    def push(self,data):
        self.stack.append(data)
        self.size += 1
# 弹栈
    def pop(self):
        if self.stack is not None:
            temp = self.stack.pop()
            self.size -= 1
        return temp
# 顶点值
    def peek(self):
        if self.stack is not None:
            return self.stack[-1]
# 是否空
    def is_empty(self):
        return not bool(self.stack)
# 数组长度
    def size(self):
        return str(self.size)
if __name__ == '__main__':
    stack =Stack(5)
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(3):
        stack.pop()
    print(stack)
    # print(stack.peek())
    # print(stack.is_empty())
    # print(stack.size)


















