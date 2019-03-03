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
def select(path, name):
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


# 保存数据
def save(path, obj):
    user_path = os.path.join(path, '%s.json' % obj.name)
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


def select_user(name):
    path = setting.BASE_USER_DB
    return select(path, name)


def save_user(obj):
    path = setting.BASE_USER_DB
    save(path, obj)


# 获取user列表
def get_user_list():
    path = setting.BASE_USER_DB
    return listdir(path)


def select_group_chat(name):
    path = setting.BASE_GROUP_CHAT_DB
    return select(path, name)


def save_group_chat(obj):
    path = setting.BASE_GROUP_CHAT_DB
    save(path, obj)


# 获取群聊列表
def get_group_chat_list():
    path = setting.BASE_GROUP_CHAT_DB
    return listdir(path)



if __name__ == '__main__':
    from lib.Student import Student
    us = Student('xm', '123')
    print(save_user('student', us))
    print(select_user('student', 'xm'))