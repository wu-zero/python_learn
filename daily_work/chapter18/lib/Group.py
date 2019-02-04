class Group:
    def __init__(self, name='', teacher_name=None):
        self.__name = name
        self.__teacher_name = teacher_name
        self.__student_name_score_dict = {}

    @property
    def name(self):
        return self.__name

    @property
    def teacher_name(self):
        return self.__teacher_name

    def set_teacher_name(self, teacher_name):
        if not self.__teacher_name:
            self.__teacher_name = teacher_name
            return True, "老师设置成功"
        else:
            return False, "该班级已有老师"

    def add_student_name(self, student_name):
        if student_name in self.__student_name_score_dict:
            return False, "学生已存在"
        else:
            self.__student_name_score_dict[student_name] = 0
            return True, "学生添加成功"

    def get_all_student_score(self):
        return self.__student_name_score_dict

    def get_student_score(self, student_name):
        if student_name in self.__student_name_score_dict:
            return self.__student_name_score_dict[student_name]
        else:
            return None

    def change_student_score(self, student_name, score):
        if student_name in self.__student_name_score_dict:
            self.__student_name_score_dict[student_name] = score
            return True, "更改成功"
        else:
            return False, "没有该学生"

    def __str__(self):
        return "班级:%s,老师:%s" % (self.name, self.teacher_name)

    @classmethod
    def create(cls):
        group_name = input("班级名称:")
        group = Group(group_name)
        return group


if __name__ == '__main__':

    group1 = Group('一班')
    print(group1.set_teacher_name('李老师'))
    print(group1.add_student_name('小明'))
    print(group1.add_student_name('小红'))
    print(group1.get_all_student_score())
    print(group1.get_student_score('小明'))
    print(group1.change_student_score('小明', 100))
    print(group1.change_student_score('小红', 99))
    print(group1.get_all_student_score())
    print(group1)
