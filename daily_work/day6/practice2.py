import numpy as np


def buy(money):
    goods_dict = {'apple': 3,
            'banana': 5
             }
    print(goods_dict.keys())
    goods_price = 0
    while True:
        input_str = input('buy goods(such as apple) number(such 5)  ')
        input_str_split = input_str.split(' ')
        if len(input_str_split) == 1 and input_str_split[0] == 'q':
            if goods_price <= money:
                print('买成功，你还有%d' %(money-goods_price))
                return
            else:
                print('你没有足够的钱')
                return
        elif len(input_str_split) == 3:
            goods, number = input_str_split[1],input_str_split[2]
            if goods in goods_dict:
                goods_price += goods_dict[input_str_split[1]] * int(input_str_split[2])


user_login_data = {}
user_locked = []
with open('data.txt', 'r') as f:
    for line in f:
        line_split = line.split(sep='|')
        name, password = line_split[0], line_split[1][:-1]
        user_login_data[name] = password

with open('data2.txt', 'r') as f:
    for line in f:
        user_locked.append(line)


while True:
    name = input('请输入姓名: ')
    if name in user_login_data.keys():
        if name in user_locked:
            print('您被锁定了，无法登陆')
            exit()
        else:
                user_login_error_time = 0
                while True:

                    if user_login_error_time >= 3:
                        print('您被锁定了')
                        user_locked.append(name)
                        np.save('data2.txt', user_locked)
                        with open('data2.txt', 'w') as f:
                            for name in user_locked:
                                f.write(name)
                        exit()

                    password = input('请输入密码: ')
                    if user_login_data[name] == password:
                        print('已登录')
                        money = input('你有多少钱')
                        buy(int(money))
                        exit()
                    else:
                        print('密码错误')
                        user_login_error_time += 1
    else:
        print('没有该用户')
