from lib.User import User


class Student(User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.__group_data_list = []

    @property
    def group_data_list(self):
        return self.__group_data_list

    def add_group(self, school, course, group):
        if [school, course, group] in self.__group_data_list:
            return False, "已添加过该班级"
        else:
            self.__group_data_list.append([school, course, group])
            return True, "添加班级成功"


if __name__ == '__main__':
    stu1 = Student('xm', '123')
    print(stu1.add_group('xm', 'xx', 'xx'))
    print(stu1.add_group('xm', 'xx', 'xx'))
    print(stu1.group_data_list)