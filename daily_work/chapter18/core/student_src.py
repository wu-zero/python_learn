from interface import common, student

user_data = {
    'name': None
}


def logout():
    user_data['name'] = None


def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    count = 0
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flag, msg = student.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count == 3:
                common.lock_user_interface(name)
                print('尝试过多，锁定')
                break


def register(): 
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码:').strip()
        conf_password = input('请确认密码:').strip()
        if password == conf_password:
            flag, msg = student.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def student_login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


@student_login_auth
def choose_group():
    print("已有学校列表:", end='')
    print(common.get_school_list_interface())
    school_name = input("输入要选择的学校:")
    print("已有课程列表:", end='')
    print(common.get_course_list_interface(school_name))
    course_name = input("输入要选择的课程:")
    print("已有班级列表:", end='')
    print(common.get_group_list_interface(school_name, course_name))
    group_name = input("输入班级名称:")
    flg, msg = common.add_group_student_interface(school_name, course_name, group_name, user_data['name'])
    print(msg)
    return flg


@student_login_auth
def check_score():
    group_list = student.get_student_group(user_data['name'])
    for group in group_list:
        print(group, ':',end='')
        print(common.get_student_score(group[0], group[1], group[2],user_data['name']))


func_dic = {
    '1': login,
    '2': register,
    '3': choose_group,
    '4': check_score,
    '5': logout
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、选课
        4、查成绩
        5、退出登陆
        q、退出
        ''')
        choice = input('请选择:').strip()
        if choice == 'q':
            logout()
            break
        if choice in func_dic:
            func_dic[choice]()


if __name__ == '__main__':
    run()
    