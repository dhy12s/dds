from typing import Any, Optional, NoReturn


class Node:
    def __init__(self, data: Any, next: Optional = None):
        self.data: Any = data
        self.next: Optional[Node] = next

    def __repr__(self):
        return f"Node({self.data})"


class LinkStack:
    def __init__(self) -> NoReturn:
        self.top = None

    def push(self, array: Any) -> None:
        node: Node = Node(array)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self) -> Any:
        if self.top is None:
            raise IndexError("pop from empty stack")
        else:
            node: Node = self.top
            self.top = node.next
            return node.data

    def is_empty(self) -> bool:
        return self.top is None

    def __repr__(self):
        cur = self.top
        string = ""
        while cur:
            string += f"{cur} --> "
            cur = cur.next
        return string + "end"


if __name__ == '__main__':
    stack = LinkStack()
    stack.push(5)
    stack.push(2)
    stack.push('abc')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.is_empty())
