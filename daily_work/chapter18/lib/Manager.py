from lib.User import User


class Manager(User):
    def __init__(self, name, password):
        super().__init__(name, password)
