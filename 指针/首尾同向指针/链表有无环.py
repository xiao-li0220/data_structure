class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def circle(head):
    fast = head
    slow = head
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

if __name__ == '__main__':
    a1=Node(1)
    a2=Node(2)
    a3=Node(3)
    a4=Node(4)
    a5=Node(5)
    a6=Node(6)
    a7=Node(7)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7
    a7.next = None
    print(circle(a1))