from typing import List


class Node:  # 结点类
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):  # 重写方法
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def insert_jiedian(self, data):
        new_jiedian = Node(data)
        if self.head:  # self.head不为None时
            new_jiedian.next = self.head
        self.head = new_jiedian

    def print_list(self):
        temp = self.head
        while temp:  # temp不为None时
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"

    def append(self, data):
        if self.head is None:
            self.insert_jiedian(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def insert(self, index, data):
        if self.head is None or index == 1:
            self.insert_jiedian(data)
        else:
            new_node = Node(data)
            curr = self.head
            prev = curr
            j = 1
            while j < index:
                prev = curr
                curr = curr.next
                j += 1
            prev.next = new_node
            new_node.next = curr

    def linklist(self, obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    def del_head(self):
        if self.head is None:
            raise Exception('空链表')
        else:
            self.head = self.head.next

    def pop(self):
        curr = self.head
        if self.head is None:
            raise Exception('空链表')
        else:
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
        return temp

    def del_tail(self,data):
        if self.head is None:
            raise Exception('空链表')
        else:
            new_node = Node(data)
            curr = self.head
            prev = curr
            while curr.next:
                prev = curr
                curr = curr.next
            else:
                temp = curr
                prev.next = None
        return temp


if __name__ == '__main__':
    a = LinkList()
    # a.insert_jiedian(4)
    # a.append(3)
    # a.insert(2,100)
    # print(a)
    # print('>>>>>>>>>>>>>>>>>>>>>>>')
    # a.print_list()
    # a.append(2)
    # a.insert_jiedian(1)
    a.linklist([1, 2, 3, 4])
    a.insert(2, 100)
    a.append(200)
    a.insert_jiedian(300)
    a.del_head()
    a.pop()
    print(a)
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    a.print_list()
