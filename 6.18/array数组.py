class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity  # 数组长度
        self.size = 0  # 数组元素个数

    def insert(self, index, element):  # index：插入的位置。element：插入的数
        """
        :param index: 插入的位置
        :type index:int
        :param element: 插入的数
        :type element:any
        :return:
        :rtype:
        """
        if index < 0 or index > self.size:
            raise Exception('越界')
        if self.size >= len(self.array):
            self.kuojie()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def shuchu(self):
        for i in range(self.size):
            print(self.array[i], end='->')

    def kuojie(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1


if __name__ == '__main__':
    array = Array(3)
    array.insert(0, 0)
    array.insert(1, 1)
    array.insert(2, 2)
    array.insert(3, 3)
    array.insert(2,2)
    array.remove(2)
    array.shuchu()
