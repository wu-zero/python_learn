class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__locked = False

    @property
    def name(self):
        return self.__name

    def check_login_info(self, password):
        if password == self.__password and self.__locked is False:
            return True
        else:
            return False

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False



if __name__ == '__main__':
    user1 = User('xm', '123')

