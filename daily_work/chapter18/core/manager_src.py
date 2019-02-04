from interface import manager, common


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
        flag, msg = manager.login_interface(name, password)
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
            flag, msg = manager.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')
      

def manager_login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_data['name']:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


@manager_login_auth
def create_school():
    print('=' * 15, "创建学校", '=' * 15)
    school_list = common.get_school_list_interface()
    print("已有学校列表:")
    print(school_list)
    flg, msg = manager.create_school_interface()
    print(msg)
    return flg


@manager_login_auth
def create_course():
    print('=' * 15, "添加课程", '=' * 15)
    school_list = common.get_school_list_interface()
    print("已有学校列表:")
    print(school_list)
    school_name = input("输入要选择的学校:")
    print("已有课程列表:")
    print(common.get_course_list_interface(school_name))
    flg, msg = manager.create_course_interface(school_name)
    print(msg)
    return flg


@manager_login_auth
def create_group():
    print('=' * 15, "添加班级", '=' * 15)
    school_list = common.get_school_list_interface()
    print("已有学校列表:", end='')
    print(school_list)
    school_name = input("输入要选择的学校:")
    print("已有课程列表:", end='')
    print(common.get_course_list_interface(school_name))
    course_name = input("输入要选择的课程:")
    print("已有老师列表:", end='')
    print(common.get_teacher_list_interface(school_name))
    teacher_name = input("输入班级老师:")
    print("已有班级列表:", end='')
    print(common.get_group_list_interface(school_name, course_name))
    flg, msg = manager.create_group_interface(school_name, course_name, teacher_name)
    print(msg)
    return flg


@manager_login_auth
def create_teacher():
    print('=' * 15, "添加老师", '=' * 15)
    school_list = common.get_school_list_interface()
    print("已有学校列表:")
    print(school_list)
    school_name = input("输入要选择的学校:")
    flg, msg = manager.create_teacher_interface(school_name)
    print(msg)
    return flg


@manager_login_auth
def set_group_teacher():
    print('=' * 15, "添加班级", '=' * 15)
    print("已有学校列表:", end='')
    print(common.get_school_list_interface())
    school_name = input("输入要选择的学校:")
    print("已有课程列表:", end='')
    print(common.get_course_list_interface(school_name))
    course_name = input("输入要选择的课程:")
    print("已有班级列表:", end='')
    print(common.get_group_list_interface(school_name, course_name))
    group_name = input("输入班级名称:")
    print("已有老师列表:", end='')
    print(common.get_teacher_list_interface(school_name))
    teacher_name = input("输入要设置的老师:")
    flg, msg = manager.set_group_teacher_interface(school_name,course_name,group_name,teacher_name)
    print(msg)
    return flg


@manager_login_auth
def check_data():
    common.show()


func_dic = {
    '1': login,
    '2': register,
    '3': create_school,
    '4': create_course,
    '5': create_group,
    '6': create_teacher,
    '7': set_group_teacher,
    '8': check_data,
    '9': logout,
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、创建学校
        4、创建课程
        5、创建班级
        6、创建老师
        7、设置班级老师
        8、查看现有信息
        9、退出登陆
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
