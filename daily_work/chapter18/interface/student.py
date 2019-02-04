from db import db_handler
from lib import base

import interface.common as common


STATUS = 'student'
user_logger = base.get_logger('student')


def login_interface(name, password):
    return common.login_interface(STATUS, name, password)


def register_interface(name, password):
    user = db_handler.select(STATUS, name)
    if user:
        return False, '用户已经存在'
    else:
        from lib.Student import Student
        new_manager = Student(name, password)
        db_handler.save(STATUS, new_manager)
        user_logger.info('%s 注册了' % name)
        return True, '注册成功'


def lock_user_interface(name):
    common.lock_user_interface(STATUS, name)


def un_lock_user_interface(name):
    common.un_lock_user_interface(STATUS, name)


def get_student_group(student_name):
    student = db_handler.select('student',student_name)
    return student.group_data_list


if __name__ == '__main__':
    print(login_interface('学生1', '123'))
    print(register_interface('学生1', '1111'))
    print(get_student_group('学生1'))