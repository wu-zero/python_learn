from db import db_handler
import interface.common as common


from lib import base

user_logger = base.get_logger('teacher')
STATUS = 'teacher'


def login_interface(name, password):
    return common.login_interface(STATUS, name, password)


def register_interface(name, password):
    user = db_handler.select(STATUS, name)
    if user:
        return False, '用户已经存在'
    else:
        from lib.Teacher import Teacher
        new_user = Teacher(name, password)
        db_handler.save(STATUS, new_user)
        user_logger.info('%s 注册了' % name)
        return True, '注册成功'


def lock_user_interface(name):
    common.lock_user_interface(STATUS, name)


def un_lock_user_interface(name):
    common.un_lock_user_interface(STATUS, name)


def get_teacher_group(teacher_name):
    teacher = db_handler.select('teacher', teacher_name)
    return teacher.group_data_list
