from db.db_handler import select_user, save_user, get_user_list
from lib import base

user_logger = base.get_logger('user')


def login_interface(name, password):
    user = select_user(name)
    if user:
        if user.check_login_info(password):
            user_logger.info('%s登录了' % name)
            return True, '登陆成功'
        else:
            return False, '用户密码错误或已经锁定'
    else:
        return False, '用户不存在'


def register_interface(name, password):
    user = select_user(name)
    if user:
        return False, '用户已经存在'
    else:
        from lib.User import User
        new_user = User(name, password)
        save_user(new_user)
        user_logger.info('%s 注册了' % name)
        return True, '注册成功'



def lock_user_interface(name):
    user = select_user(name)
    if user:
        user.lock()
        save_user(user)
        user_logger.info('%s被锁定了' % name)


def un_lock_user_interface(name):
    user = select_user(name)
    if user:
        user.unlock()
        save_user(user)
        user_logger.info('%s解锁了' % name)

def get_friend_list(name):
    user = select_user(name)
    if user:
        return user.friends_list

def add_friend_interface(name):
    user = select_user(name)
    if user:
        users_list = get_user_list()
        print(users_list)
        friend_name = input('输入朋友姓名')
        if friend_name in users_list:
            user.add_friend(friend_name)
            save_user(user)
            friend = select_user(friend_name)
            friend.add_friend(name)
            save_user(friend)

            return True, '添加成功'
        else:
            return False, '没有该用户'
