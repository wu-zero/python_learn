class GroupChat:
    def __init__(self, name):
        self.__name = name
        self.__users_list = []

    @property
    def name(self):
        return self.__name

    @property
    def users_list(self):
        return self.__users_list


    def add_user(self, user_name):
        self.__users_list.append(user_name)



if __name__ == '__main__':
    gc = GroupChat('群聊1')
    gc.add_user('xiaoming')
    print(gc.users_list)
