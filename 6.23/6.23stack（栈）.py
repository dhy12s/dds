class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) < self.size:
            raise Exception("stackoverflow")
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError("pop from an empty stack")

    def peak(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return self.size


if __name__ == '__main__':
    stack = Stack(5)
    for i in range(10):
        stack.push(i)
    print(stack)
