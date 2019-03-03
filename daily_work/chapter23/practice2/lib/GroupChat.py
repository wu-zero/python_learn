class GroupChat:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []

    @property
    def name(self):
        return self.__name

    @property
    def user_list(self):
        return [user[0] for user in self.__user_list]

    @property
    def user_list_and_port(self):
        return self.__user_list

    def add_user(self, user_name, user_ip_port):
        self.__user_list.append([user_name, user_ip_port])



if __name__ == '__main__':
    gc = GroupChat('群聊1')
    gc.add_user('xiaoming','192....')
    print(gc.user_list)
