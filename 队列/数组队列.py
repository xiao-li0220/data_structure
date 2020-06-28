class Queue:
    def __init__(self):
        self.entries = []
        self.front = 0
        self.size = 0
    def __repr__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed
    # 入队 enqueue
    def put(self,data):
        self.entries.append(data)
        self.size += 1
    # 出队 dequeue
    def pop(self):
        self.size -= 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued
    def length(self):
        return self.size
    def head(self):
        return self.entries[0]
    def rotate(self,rotation):
        for i in range(rotation):
            self.put(self.get())

q = Queue()
q.put(2)
q.put(1)
q.put(66)
print(q)
print(q.pop())
print(q)
print(q.head())
print(q.length())
