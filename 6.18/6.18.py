class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print('%s可以自主学习' % (self.name))


a = input('请输入姓名：')
name1 = Student(a)
name1.study()

s = 'asdsaa'
print(s.count('a'))
