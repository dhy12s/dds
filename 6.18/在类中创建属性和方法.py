class Person:
    # 构造方法: 设置对象的属性 __init__ (初始化)
    # 当实例化(创建)对象的时候执行
    def __init__(self,a,b,c):
        # self: 相当于每次创建好的对象
        self.name = a
        self.age = b
        self.height = c
    def eat(self):
        print('%s吃饭'%(self.name))

# 实例化对象 (创建对象)
p = Person('小明',20,180)
print(p.name,p.age,p.height)
# 实例化第二个对象
p1 = Person('小红',30,150)
print(p1.name,p1.age,p1.height)
# 方法掉用
p.eat()
p1.eat()

# 设置属性
# print(id(p))
# # p.name = '小明'
# 调用方法
# p.eat()