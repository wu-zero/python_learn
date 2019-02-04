from lib.User import User


class Teacher(User):
    def __init__(self, name, password='123'):
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

    @classmethod
    def create(cls):
        teacher_name = input("老师姓名:")
        teacher = Teacher(teacher_name)
        return teacher
      
if __name__ == '__main__':
    teacher1 = Teacher('xm', 'sss')
    print(teacher1.add_group('xm', 'xx', 'xx'))
    print(teacher1.add_group('xm', 'xx', 'xx'))
    print(teacher1.group_data_list)
