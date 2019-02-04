from db import db_handler
from lib import base

from interface import common

STATUS = 'manager'
user_logger = base.get_logger('manager')


# ===============登录注册相关===============
def login_interface(name, password):
    return common.login_interface(STATUS, name, password)


def register_interface(name, password):
    user = db_handler.select(STATUS, name)
    if user:
        return False, '用户已经存在'
    else:
        from lib.Manager import Manager
        new_manager = Manager(name, password)
        db_handler.save(STATUS, new_manager)
        user_logger.info('%s 注册了' % name)
        return True, '注册成功'


def lock_user_interface(name):
    common.lock_user_interface(STATUS, name)


def un_lock_user_interface(name):
    common.un_lock_user_interface(STATUS, name)


# ===============功能相关===============
def create_school_interface():
    from lib.School import School
    new_school = School.create()
    return common.add_school_interface(new_school)


def create_course_interface(school_name):
    from lib.Course import Course
    new_course = Course.create()
    return common.add_course_interface(school_name, new_course)


def create_group_interface(school_name, course_name, teacher_name):
    from lib.Group import Group
    new_group = Group.create()
    flag, msg = common.add_group_interface(school_name, course_name, new_group)
    return common.set_group_teacher_interface(school_name, course_name, new_group.name, teacher_name)


def create_teacher_interface(school_name):
    from lib.Teacher import Teacher
    new_teacher = Teacher.create()
    if new_teacher.name in common.get_user_list_interface('teacher'):
        return False, "该老师已存在"
    else:
        db_handler.save('teacher', new_teacher)
        return common.add_teacher_interface(school_name, new_teacher)


def set_group_teacher_interface(school_name, course_name, group_name, teacher_name):
    return common.set_group_teacher_interface(school_name, course_name, group_name, teacher_name)


if __name__ == '__main__':
    print(register_interface('xg', '111', 'manager'))
    print(login_interface('xg', '111', 'manager'))
    print(create_school_interface())
    # print(add_course_interface())
    # print(add_group_interface())