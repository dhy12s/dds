class Queue:
    def __init__(self):
        self.list = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.list)[1:-1] + ">"
        return printed

    def put(self, item):
        self.list.append(item)
        self.length += 1

    def get(self):
        self.length = self.length - 1
        dequeued = self.list[self.front]
        self.list = self.list[1:]
        return dequeued

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def front(self):
        return self.list[0]

    def size(self):
        return self.length

q = Queue()
q.put(1)
q.put(3)
q.put(5)
print(q)
print(q.get())
print(q)
print(q.front)
print(q)
print(q.size())
print(q)
