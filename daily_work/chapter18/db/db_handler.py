import os
from conf import setting
import pickle


def listdir(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        elif os.path.splitext(file_path)[1] == '.json':
            list_name.append(file[:-5])
    return list_name


# 选数据
def select(status, name):
    if status == 'student':
        path = setting.BASE_STUDENT_DB
    elif status == 'teacher':
        path = setting.BASE_TEACHER_DB
    elif status == 'manager':
        path = setting.BASE_MANAGER_DB
    elif status == 'school':
        path = setting.BASE_SCHOOL_DB

    object_path = os.path.join(path, '%s.json' % name)
    if os.path.exists(object_path):
        if os.path.getsize(object_path) > 0:
            with open(object_path, 'rb') as f:
                obj = pickle.load(f)
                return obj
        else:
            return None
    else:
        return None


# 保存数据data_dic={'name':name,'object',object}
def save(status, obj):
    if status == 'student':
        path = setting.BASE_STUDENT_DB
    elif status == 'teacher':
        path = setting.BASE_TEACHER_DB
    elif status == 'manager':
        path = setting.BASE_MANAGER_DB
    elif status == 'school':
        path = setting.BASE_SCHOOL_DB

    user_path = os.path.join(path, '%s.json' % obj.name)
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()
    

# 获取学校目录
def get_school_list():
    path = setting.BASE_SCHOOL_DB
    return listdir(path)

# 
def get_user_list(status):
    if status == 'student':
        path = setting.BASE_STUDENT_DB
    elif status == 'teacher':
        path = setting.BASE_TEACHER_DB
    elif status == 'manager':
        path = setting.BASE_MANAGER_DB
    elif status == 'school':
        path = setting.BASE_SCHOOL_DB
    return listdir(path)


if __name__ == '__main__':
    from lib.Student import Student
    us = Student('xm', '123')
    print(save('student', us))
    print(select('student', 'xm'))
    print(get_school_list())