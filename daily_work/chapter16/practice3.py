# 3. 除了文中讲到的方法之外，另外用至少4种方式实现单例模式（有能力还可以使用更多种）补充：这一章的代码必须要在类的创建过程，调用过程和单例模式的分支语句添加注释，其他注释也可自由添加


# 元类方法
class SingletonMeta(type):
    def __init__(cls, class_name, class_base, class_dic):
        cls.__instance = None  # 保存实例化的对象,没就None
        super(SingletonMeta, cls).__init__(class_name, class_base, class_dic)

    def __call__(cls, *args, **kwargs):  # 以SingletonMeta为元类的类实例化对象的时候
        if not cls.__instance:  # 是不是实例化过了,是就返回实例化过的对象,没有就实例化,放到cls.__instance
            cls.__instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instance


class Foo(metaclass=SingletonMeta):  # 创建Foo类的type为SingletonMeta
    pass


f1 = Foo()
f2 = Foo()
print(f1 is f2)


# 装饰器方法
def singleton2(cls):
    __fun_dict = {}  # 保存对象,以类本身为key,实例化的对象为value
    
    def wrapper(*args, **kwargs):
        if cls not in __fun_dict:  # 这个类是不是实例化过对象了
            __fun_dict[cls] = cls(*args, **kwargs)  # 没有,就实例个对象存起来
        return __fun_dict[cls]

    return wrapper


@singleton2
class Foo2:
    pass


f1 = Foo2()
f2 = Foo2()
print(f1 is f2)


# 模块单例
from practice3_Singleton3 import singleton as singleton3
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
# 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。

f1 = singleton3
f2 = singleton3
print(f1 is f2)


# 静态变量方法
class Singleton4(object):
    def __new__(cls, *args, **kwargs):  # new用于实现新实例(创建新对象),把实例化的对象放到实例化的类中
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)

        return cls._instance


f1 = Singleton4()
f2 = Singleton4()
print(f1 is f2)



