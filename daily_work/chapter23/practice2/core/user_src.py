import socket
from conf.setting import SERVER_IP_PORT
from interface import user_interface
from conf.setting import SERVER_IP_PORT
import conf.command as cm
import struct



client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

user_now_name = None

def logout():
    global user_now_name
    client.sendto(struct.pack('i', cm.LogoutCommand) + user_now_name.encode('utf-8'), SERVER_IP_PORT)
    user_now_name = None


def login():
    global user_now_name
    print('登陆')
    if user_now_name is not None:
        print('您已经登陆了')
        return
    count = 0
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()
        flg, msg = user_interface.login_interface(name, password)
        if flg:
            user_now_name = name
            client.sendto(struct.pack('i', cm.LoginCommand)+user_now_name.encode('utf-8'), SERVER_IP_PORT)
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count == 3:
                user_interface.lock_user_interface(name)
                print('尝试过多，锁定')
                break


def register():
    global user_now_name
    print('注册')
    if user_now_name:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码:').strip()
        conf_password = input('请确认密码:').strip()
        if password == conf_password:
            flag, msg = user_interface.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not user_now_name:
            login()
        else:
            return func(*args, **kwargs)
    return wrapper


@login_auth
def send_message_to_friend():

    print(user_interface.get_friends_list(user_now_name))
    friend_name = input("朋友名字:")
    while True:
        messages = input("信息>>").strip().encode('utf-8')
        if not messages:
            print("不能为空...")
            continue
        elif messages == b'q':
            break
        else:
            messages = (friend_name + '|').encode('utf-8') + messages
            client.sendto(struct.pack('i', cm.ChatCommand) + messages, ('127.0.0.1', 8080))
            # data, addr = client.recvfrom(1024)
            # print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
    # client.close()



@login_auth
def receive_message_to_friend():
    while True:
        data, addr = client.recvfrom(1024)
        print(data.decode('utf-8'))



@login_auth
def send_message_to_group():
    print(user_interface.get_groups_list(user_now_name))
    group_name = input("群聊名称:")
    while True:
        messages = input("信息>>").strip().encode('utf-8')
        if not messages:
            print("不能为空...")
            continue
        elif messages == b'q':
            break
        else:
            messages = (group_name + '|').encode('utf-8') + messages
            client.sendto(struct.pack('i', cm.GroupChatCommand) + messages, ('127.0.0.1', 8080))
            # data, addr = client.recvfrom(1024)
            # print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
    # client.close()

@login_auth
def add_friend():
    print("已有好友")
    print(user_interface.get_friends_list(user_now_name))
    user_interface.add_friend_interface(user_now_name)

@login_auth
def add_group_chat():
    print("已有群")
    print(user_interface.get_groups_list(user_now_name))
    user_interface.add_group_interface(user_now_name)


func_dic = {
    '1': login,
    '2': register,
    '3': send_message_to_friend,
    '4': receive_message_to_friend,
    '5': send_message_to_group,
    '7': add_friend,
    '8': add_group_chat,
    '9': logout

}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、发消息
        4、接受信息
        5、给群发消息
        7、添加朋友
        8、添加群聊
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
