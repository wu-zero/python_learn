from db.db_handler import select_user, save_user, get_user_list,select_group_chat,save_group_chat,get_group_chat_list
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

def get_friends_list(name):
    user = select_user(name)
    if user:
        return user.friends_list

def get_groups_list(name):
    user = select_user(name)
    if user:
        return user.groups_list



def add_friend_interface(name):
    user = select_user(name)
    if user:
        users_list = get_user_list()
        print("用户列表")
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

def add_group_interface(name):
    user = select_user(name)
    if user:
        group_list = get_group_chat_list()
        print("群列表")
        print(group_list)

        group_name = input("输入群名:")

        group = select_group_chat(group_name)
        if group is not None:
            group.add_user(name)
            save_group_chat(group)
            user.add_group_chat(group_name)
            save_user(user)
            user_logger.info('%s 加入了%s' % (name, group_name))
        else:
            flg = input("是否建群? 1 yes, 2 no")
            if flg == '1':
                from lib.GroupChat import GroupChat
                group = GroupChat(group_name)
                group.add_user(name)
                save_group_chat(group)
                user.add_group_chat(group_name)
                save_user(user)
            elif flg == '2':
                pass
            else:
                pass


