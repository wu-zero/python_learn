
import conf.command as cm
from interface import common
import socket

user_dict = {}
online_user = []
group_dict = {}

def solve_data(data):
    import struct
    command = struct.unpack('i', data[:4])[0]
    message = data[4:].decode('utf-8')
    return command, message

def from_address_get_name(address):
    for i_name, i_address in user_dict.items():
        if address[1] == i_address[1]:
            return i_name
    return None


def run(ip):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 数据报协议
    server.bind(ip)

    while True:
        data, addr = server.recvfrom(1024)

        sender = from_address_get_name(addr)
        command, message = solve_data(data)
        if command == cm.LoginCommand:
            name = message
            user_dict[name] = addr
            online_user.append(name)
        elif command == cm.LogoutCommand:
            name = message
            del user_dict[name]
            online_user.remove(name)
        elif command == cm.ChatCommand:
            message_list = message.split('|')
            friend_name = message_list[0]
            message = (sender + '：'+message_list[1]).encode('utf-8')
            if friend_name in online_user:
                friend_address = user_dict[friend_name]
                server.sendto(message, friend_address)
            # else:
            #     server.sendto(message, addr)

        elif command == cm.GroupChatCommand:
            message_list = message.split('|')
            group_name = message_list[0]
            message = (sender + '：' + message_list[1]).encode('utf-8')
            group_dict = common.get_group_dict_interface()
            if group_name in group_dict.keys():
                group_users = group_dict[group_name]
                for user in group_users:
                    if user in online_user:
                        friend_address = user_dict[user]
                        server.sendto(message, friend_address)



            # else:
            #     server.sendto(message, addr)



        # print(online_user)
        # print(user_dict)
    server.close()