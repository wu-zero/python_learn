from interface import common, teacher

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
        flag, msg = teacher.login_interface(name, password)
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
    print("注册窗口暂未开放")
    # print('注册')
    # if user_data['name']:
    #     print('您已经登陆了')
    #     return
    # while True:
    #     name = input('请输入名字:').strip()
    #     if name == 'q':
    #         break
    #     password = input('请输入密码').strip()
    #     conf_password = input('请确认密码').strip()
    #     if password == conf_password:
    #         flag, msg = teacher.register_interface(name, password)
    #         if flag:
    #             print(msg)
    #             break
    #         else:
    #             print(msg)
    #     else:
    #         print('两次密码不一致')


def teacher_login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


@teacher_login_auth
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


@teacher_login_auth
def check_score():
    group_list = teacher.get_teacher_group(user_data['name'])
    for group in group_list:
        print(group, ':', end='')
        print(common.get_all_student_score(group[0], group[1], group[2]))


@teacher_login_auth
def change_student_score():
    group_list = teacher.get_teacher_group(user_data['name'])
    for i in range(len(group_list)):
        print(i, '|', group_list[i])
    group_i = int(input("输入你选择的班级标号"))
    school_name, course_name, group_name = group_list[group_i]
    while True:
        print(common.get_all_student_score(school_name, course_name, group_name))
        student_name = input("学生姓名:(q退出)")
        if student_name == 'q':
            break
        score = int(input("分数:"))
        flg, msg = common.set_student_score(school_name, course_name, group_name, student_name, score)
        print(msg)


func_dic = {
    '1': login,
    '2': register,
    '3': choose_group,
    '4': check_score,
    '5': change_student_score,
    '6': logout
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、选课
        4、查成绩
        5、改成绩
        6、退出登陆
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
    