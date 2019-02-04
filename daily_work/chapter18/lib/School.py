from lib.Teacher import Teacher
from lib.Course import Course


class School:
    def __init__(self, name):
        self.__name = name
        self.__teacher_name_list = []
        self.__course_dict = {}

    @property
    def name(self):
        return self.__name

    @property
    def teacher_list(self):
        return self.__teacher_name_list

    @property
    def course_list(self):
        return list(self.__course_dict.keys())


    # school
    def add_teacher(self, teacher_name):
        if teacher_name in self.__teacher_name_list:
            return False, "老师已存在"
        else:
            self.__teacher_name_list.append(teacher_name)
            return True, "老师添加成功"

    def add_course(self, new_course):
        if new_course.name in self.course_list:
            return False, "课程已存在"
        else:
            self.__course_dict[new_course.name] = new_course
            return True, "课程添加成功"

    def get_course_from_name(self, course_name):
        if course_name in self.course_list:
            return self.__course_dict[course_name]
        else:
            return None

    def get_group_from_name(self, course_name, group_name):
        course = self.get_course_from_name(course_name)
        if course is None:
            return None
        else:
            return course.get_group_from_name(group_name)

    def add_group(self, course_name, new_group):
        course = self.get_course_from_name(course_name)
        if course is None:
            return False, "课程不存在"
        else:
            return course.add_group(new_group)

    def __str__(self):
        return "学校名称:%s\n教师列表:%s \n课程列表:%s" % (self.name, ','.join(self.teacher_list), ','.join(self.course_list))

    def show(self):
        print('='*30)
        print(self)
        print("课程信息:")
        if self.__course_dict == {}:
            print("暂无课程")
        else:
            for course_name, course in self.__course_dict.items():
                course.show()

    @classmethod
    def create(cls):
        school_name = input("学校名称:")
        school = School(school_name)
        return school


if __name__ == '__main__':
    sch = School('上海')

    print(sch.add_teacher('xm'))
    # print(sch.course_list)
    # sch.show_teacher_list()
    # sch.show_course_list()
    # sch.show_group_list()
    #print(sch)
    sch.show()