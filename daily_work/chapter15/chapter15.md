# chapter15
### 一、简答题
#### 1. 类的属性和对象的属性有什么区别?
>对象是类的实例，类是相同结构的对象的抽象。同类的各个对象其实拥有相同的属性和方法，只是属性值不同而已。好比学生类中的学生对象，每个学生的属性(身高，学号等)  
类的属性说的应该就是静态变量(static修饰符)就是在类加载的时候，就已被分配了内存(存在于静态区)只有一份，所以new出来的对象都共享此属性。而对象的属性就非static修饰的属性，是属于单个实例化的类。每new一个实例就在堆内存中创建一份。就等于多个拷贝，占内存多，但比较灵活，自己修改自己的属性值，互不影响。  
来源：https://blog.csdn.net/j904538808/article/details/79157634 
#### 2. 什么是绑定到对象的方法，如何定义，如何调用，给谁用？有什么特性
类里普通定义的的方法(不加@classmethod装饰器修饰)都是绑定到对象的，给对象用，`obj.method()`调用，自动把`obj`作为第一个参数传入。  
类也可以调用，但是必须把对象传入作为第一个参数。
#### 3. 什么是多态,多态有哪些优点,可以在哪些场景使用多态
[参考](https://www.cnblogs.com/hai-ping/articles/2807750.html)
#### 4. 以自己的理解简述一下Python中鸭子类型,可以查阅资料,举出一个简单实例(代码实现)

[参考](https://zh.wikipedia.org/wiki/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B#%E5%9C%A8Python%E4%B8%AD)
[参考2](https://blog.csdn.net/zhchs2012/article/details/79273109)
#### 5. 什么是封装,封装有哪些优点
封装的核心是“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。  
封装数据：保护隐私  
封装方法：隔离复杂度  

#### 6. 教程中封装那一节的小问题


### 二、代码优化
#### 10. 如下示例, 在没有学习类这个概念时，数据与功能是分离的，请用面向对象的形式优化以下代码
```python
def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
def exc2(host,port,db,charset,proc_name):
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx
# 每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
```
见`practice10.py`

### 三、代码解释
#### 11. 不运行程序看代码说出代码运行结果并解释
```python
class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```
见`practice11.py`

### 四、程序设计
#### 12. 使用组合与继承设计一个学生选择课程的程序
    使老师和学生初始化都具有课程属性,但是属性值为空,可以动态添加,可打印出老师教授的的课程和学生学习的课程,可以打印出课程名字和价格,尽量避免写重复代码
    （提示：学生和老师都是属于人,都有课程属性）

见`practice12.py`
#### 13. 使用多态与封装设计一个虚拟宠物的程序

    三个基础的宠物类 -- Cat类,Dog类,Pig类
    属性：name(名字)、type(品种),name、type均为私有属性(对内可见,对外不可见)
    type属性为成员属性(由构造器__init__方法赋初值),但type对外又是可读可写(利用property装饰器实现),name属性初始化操作由父类完成(子类利用super()来实现)
    方法：eat(self)  均拥有eat的方法(父级继承)  但实现体分别可以体现出 "吃猫粮"、"吃狗粮"、"吃猪粮"不同点(不同的实现)  

    一个宠物的父类 -- Pet类  
    属性：name(名字),name为私有属性(对内可见,对外不可见),name属性为成员属性(由构造器__init__方法赋初值),但name对外又是可读可写(利用property装饰器实现)
    方法：eat(self),拥有eat的方法(没有方法的实现体,利用abc模块实现)

    一个主人类 -- Master类
    属性：name(名字)、pet(宠物),name、pet均为私有成员属性(具体操作同上面属性的操作)
    方法：feed(self),拥有feed方法(方法只有self一个参数,没有多余的参数),feed方法实现要求:
    -- "某某"主人准备好宠物粮食  
    -- "某某品种"的"某某宠物"来进食  
    -- 吃...(调用宠物自身的eat方法) 
    注：""括起来的某某都是要被替换为具体的数据的创建三个宠物主人,分别养的是不同的三种宠物三个主人进行喂食的时候,对应养的宠物就会完成进食其他细节自由补充

见`practice13.py`

