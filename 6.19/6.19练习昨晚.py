class Array:
    def __init__(self, capacity):
        self.array = [None] * 2 * capacity
        self.size = 0

    def insert(self, index, element):
        """
        :param index:
        :type index:
        :param element:
        :type element:
        :return:
        :rtype:
        """
        if index < 0 or index > self.size:
            raise Exception('越界')
        if self.size >= len(self.array):
            self.kuojie()
        for i in range(self.array - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def kuojie(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def shuchu(self):
        for i in range(self.size):
            print(self.array[i], end='-->')

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

"""
:Author:  Mr.Dong
:Create:  2020/6.23/19 10:04
:Github:  null
Copyright (c) 2020, Mr.Dong Group All Rights Reserved.
"""