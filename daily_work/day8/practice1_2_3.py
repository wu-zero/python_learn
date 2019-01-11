# 1 编写函数，（函数执行的时间是随机的）
# 2 编写装饰器，为函数加上统计时间的功能
# 3 编写装饰器，为函数加上认证的功能
# 4 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
#     要求：
#         登录成功一次，后续的函数都无需再输入用户名和密码
#     注意：
#         从文件中读出字符串形式的字典，可以用
#         eval('{"name":"albert","password":"123"}')转成字典格式
#
# 5 编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
# 6 编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 7 为题目五编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，
# 否则，就去下载，然后存到文件中
# 扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
# 8 还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，
# 在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
# 9 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取

import time
import random


# 1 编写函数，（函数执行的时间是随机的）
def sleep_random():
    print('程序开始')
    sleep_time = random.randint(1, 10)
    print('sleep时间:%ds' % sleep_time)
    time.sleep(sleep_time)
    print('程序结束')


# 2 编写装饰器，为函数加上统计时间的功能
def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('程序运行时间：%s' % (stop_time - start_time))
        return res

    return wrapper

@timmer
def sleep_random2():
    print('程序开始')
    sleep_time = random.randint(1, 10)
    print('sleep时间:%ds' % sleep_time)
    time.sleep(sleep_time)
    print('程序结束')


# 3 编写装饰器，为函数加上认证的功能
def auth(driver='file'):
    def auth2(func):
        def wrapper(*args, **kwargs):
            name = input("user: ")
            pwd = input("pwd: ")

            if driver == 'file':
                if name == 'albert' and pwd == '123':
                    print('login successful')
                    res = func(*args,**kwargs)
                    return res
            elif driver == 'ldap':
                print('ldap')
        return wrapper
    return auth2


@auth(driver='file')
def sleep_random3():
    print('程序开始')
    sleep_time = random.randint(1, 10)
    print('sleep时间:%ds' % sleep_time)
    time.sleep(sleep_time)
    print('程序结束')

sleep_random3()