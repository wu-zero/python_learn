class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__locked = False
        self.__friends = []
        self.__group = []

    @property
    def name(self):
        return self.__name

    @property
    def friends_list(self):
        return self.__friends

    @property
    def groups_list(self):
        return self.__group

    def check_login_info(self, password):
        if password == self.__password and self.__locked is False:
            return True
        else:
            return False

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False

    def add_friend(self, friends_name):
        self.__friends.append(friends_name)

    def add_group_chat(self, group_name):
        self.__group.append(group_name)




if __name__ == '__main__':
    user1 = User('xm', '123')
    user1.add_group_chat('g1')
    print(user1.groups_list)


