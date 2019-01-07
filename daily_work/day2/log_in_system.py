# 登录系统
User = {'xm': '111111',
        'xh': '222222',
        'xg': '333333'}

User_error_time = {'xm': 0,
                    'xh': 0,
                    'xg': 0}


User_Locked = []
while True:
    name = input('请输入姓名: ')
    password = input('请输入密码: ')
    if name in User.keys():
        if name in User_Locked:
            print('您被锁定了，无法登陆')
        elif User[name] == password:
            print('已登录')
        else:
            print('密码错误')
            User_error_time[name] += 1
            if User_error_time[name] == 3:
                User_Locked.append(name)
                print('您被锁定了，无法登陆')

    else:
        print('没有该用户')