# chapter17
#### 1. 详细说一下异常常见的种类
[参考](https://www.cnblogs.com/zln1021/p/6106185.html)
#### 2. 程序设计：（以下这些是一个题目）
    自定义一个Integer类
    该类有个input方法，调用该方法一定会得到一个合法的数字(非数字为不合法，越界为不合法)
    1. 如果是非数字不合法，需要打印不合法消息，然后用户需要重新输入
    如输入'abc'，不合法消息就为：invalid literal for int() with base 10: 'abc'
    2. 如果是越界不合法，需要打印不合法消息，然后用户需要重新输入
    如输入'2147483648'，不合法消息就为：ErrorMsg：2147483648 - 越界
    提示：
    1. 该方法需要捕获并处理两次异常(内置异常ValueError，自定义异常SlopOverError)
    2. 该方法运用到递归方式处理更简单，如果用不到递归也可以
    3. 该类有个verifySlopOver方法，可以判断传入的数字是否越界(非-2147483648 ~ 2147483647为越界)
        如果数字越界，会主动抛出自定义SlopOverError异常，并传入数字和异常消息
    4. 自定义异常SlopOverError类
        该类需要重写__init__方法
        有number、massage两个参数，number是数字类型的数，massage是字符串类型的异常消息
        通过number、massage两个属性格式化异常信息
见`practice2.py`
