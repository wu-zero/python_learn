from db import db_handler
from lib import base

common_logger = base.get_logger('common')


# ===============登录注册相关===============
def login_interface(status, name, password):
    user = db_handler.select(status, name)
    if user:
        if user.check_login_info(password):
            common_logger.info('%s登录了(身份:%s)' % (name,status))
            return True, '登陆成功'
        else:
            return False, '用户密码错误或已经锁定'
    else:
        return False, '用户不存在'


def register_interface(status, name, password):
    pass


def lock_user_interface(status, name):
    user = db_handler.select(status, name)
    if user:
        user.lock()
        db_handler.save(status, user)
        common_logger.info('%s被锁定了' % name)


def un_lock_user_interface(status, name):
    user = db_handler.select(status, name)
    if user:
        user.unlock()
        db_handler.save(status, user)
        common_logger.info('%s解锁了' % name)


# all
def get_school_list_interface():
    school_list = db_handler.get_school_list()
    return school_list


def add_school_interface(new_school):
    school_list = get_school_list_interface()
    if new_school.name in school_list:
        return False, "学校已存在"
    else:
        db_handler.save('school', new_school)
        common_logger.info('%s学校创建成功' % new_school.name)
        return True, "学校创建成功"


def get_user_list_interface(status):
    user_list = db_handler.get_user_list(status)
    return user_list


def show():
    print('=' * 15, "学校信息展示", '=' * 15)
    school_name_list = get_school_list_interface()
    for school_name in school_name_list:
        school = get_school_interface(school_name)
        school.show()


# school
def get_school_interface(school_name):
    return db_handler.select('school', school_name)


def get_course_list_interface(school_name):
    school = get_school_interface(school_name)
    if school:
        return school.course_list


def add_course_interface(school_name, new_course):
    school = get_school_interface(school_name)
    if school:
        flg, msg = school.add_course(new_course)
        if flg:
            db_handler.save('school', school)
            common_logger.info('%s学校创建%s课程成功' % (school_name, new_course.name))
        else:
            pass
        return flg, msg

    else:
        return False, "学校不存在"


def get_teacher_list_interface(school_name):
    school = get_school_interface(school_name)
    if school:
        return school.teacher_list


def add_teacher_interface(school_name, teacher):
    school = get_school_interface(school_name)
    if school:
        flg, msg = school.add_teacher(teacher.name)
        if flg:
            db_handler.save('school', school)
            common_logger.info('%s学校添加%s老师成功' % (school_name, teacher.name))
        else:
            pass
        return True, "老师添加成功"
    else:
        return False, "学校不存在"


# course
def get_group_list_interface(school_name, course_name):
    school = get_school_interface(school_name)
    if school:
        course = school.get_course_from_name(course_name)
        if course:
            return course.group_list


def add_group_interface(school_name, course_name, new_group):
    school = get_school_interface(school_name)
    if school:
        flg, msg = school.add_group(course_name, new_group)
        if flg:
            db_handler.save('school', school)
            common_logger.info('%s学校%s课程创建%s班级成功' % (school_name, course_name, new_group.name))
        return flg, msg
    else:
        return False, "学校不存在"


# group
def get_group_teacher_interface(school_name, course_name, group_name):
    school = get_school_interface(school_name)
    group = school.get_group_from_name(course_name, group_name)
    return group.teacher_name


def set_group_teacher_interface(school_name, course_name, group_name, teacher_name):
    school = get_school_interface(school_name)
    if school:
        group = school.get_group_from_name(course_name, group_name)
        teacher = db_handler.select('teacher', teacher_name)
        if group and teacher:
            if teacher.name in school.teacher_list:
                flg, mag = group.set_teacher_name(teacher.name)
                if flg:
                    teacher.add_group(school_name, course_name, group_name)
                    db_handler.save('school', school)
                    db_handler.save('teacher', teacher)
                    common_logger.info('%s学校%s课程%s班级设置%s老师成功' % (school_name, course_name, group_name, teacher_name))
                return flg, mag
            else:
                return False, "该老师不在该学校"
        else:
            return False, "没有该班级或该老师"
    else:
        return False, "没有该学校"


def add_group_student_interface(school_name, course_name, group_name, student_name):
    school = get_school_interface(school_name)
    group = school.get_group_from_name(course_name, group_name)
    student = db_handler.select('student', student_name)
    if group and student:
        flg, msg = group.add_student_name(student_name)
        if flg:
            student.add_group(school_name, course_name, group_name)
            db_handler.save('school', school)
            db_handler.save('student', student)
            common_logger.info('%s学校%s课程%s班级添加%s学生成功' % (school_name, course_name, group_name, student_name))
        return flg, msg
    else:
        return False, "没有该班级或该学生"


def get_student_score(school_name, course_name, group_name, student_name):
    school = get_school_interface(school_name)
    if school:
        group = school.get_group_from_name(course_name, group_name)
        if group:
            return group.get_student_score(student_name)


def get_all_student_score(school_name, course_name, group_name):
    school = get_school_interface(school_name)
    if school:
        group = school.get_group_from_name(course_name, group_name)
        if group:
            return group.get_all_student_score()


def set_student_score(school_name, course_name, group_name, student_name, score):
    school = get_school_interface(school_name)
    if school:
        group = school.get_group_from_name(course_name, group_name)
        if group:
            flg, msg = group.change_student_score(student_name, score)
            if flg:
                db_handler.save('school', school)
                common_logger.info('%s学校%s课程%s班级设置%s学生成绩为%d' % (school_name, course_name, group_name, student_name,score))
            return flg, msg
        else:
            return False, "没有该班级"


if __name__ == '__main__':
    # print(register_interface('manager', 'xm', '111', ))
    # print(login_interface('manager', 'xm', '111', ))
    # sch = School.create()
    # print(add_school_interface(sch))
    # course = Course.create()
    # print(add_course_interface('shanghai', course))
    #group1 = Group.create()
    #print(add_group_interface('beijing', 'Python', group1))
    print(set_group_teacher_interface('shanghai','Python', '一班','laoshi1'))





