# 11. 不运行程序看代码说出代码运行结果并解释
class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x)
# 1 1 1
# Parent 的类属性x本来就是1
# Child1 和 Child2 找类属性没找到,就去自己的父类里找,也是1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
# 1 2 1
# Parent 的类属性x本来就是1
# Child1 的类属性x改为2
# Child2 找类属性没找到,就去自己的父类里找,也是1
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
# 3 2 3
# Parent 的类属性x改为3
# Child1 的类属性x为2
# Child2 找类属性没找到,就去自己的父类里找,也是3