from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def insert(self, index, data):
        newnode = Node(data)
        if index < 0 or index > self.size:
            raise Exception('越界')
        elif self.size == 0:
            self.head = newnode
            self.tail = self.head
        elif index == self.size:  # 尾
            self.tail.next = newnode
            self.tail = newnode
        elif index == 1:  # 头
            newnode.next = self.head
            self.head = newnode
        else:
            pre = self.get(index)
            newnode.next = pre.next
            pre.next = newnode
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('越界')
        elif self.size == 1:
            renode = self.head
            self.head = self.head.next
        elif index == self.size:  # 尾
            pre = self.get(index-1)
            renode = pre.next
            pre.next = None
            self.tail = pre
        else:
            pre = self.get(index)
            renode = pre.next
            pre.next = pre.next.next
        self.size -= 1

    def reserve(self):
        pre = None
        cur = self.head
        while cur:
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
        string = ""
        while cur:
            string = string + f"{cur} --> "
            cur = cur.next
        return string + 'end'


if __name__ == '__main__':
    a = LinkList()
    a.insert(0, 0)
    a.insert(1, 1)
    a.insert(2, 2)
    a.insert(3, 3)
    print(a)
    a.remove(1)
    a.remove(3)
    print(a)
    a.reserve()
    print(a)
