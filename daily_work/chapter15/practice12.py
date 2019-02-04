# 12. 使用组合与继承设计一个学生选择课程的程序,使老师和学生初始化都具有课程属性,但是属性值为空,可以动态添加,
# 可打印出老师教授的课程和学生学习的课程,可以打印出课程名字和价格,尽量避免写重复代码
# （提示：学生和老师都是属于人,都有课程属性）


class Course:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Course name:%s ,price: %s' % (self._name, self._price)

    def get_name(self):
        return self._name


class People:
    def __init__(self, name):
        self._name = name
        self._course_list = []

    def add_course(self, course):
        self._course_list.append(course)

    def print_course_data(self):
        if not self._course_list:
            print('%s没有课' % self._name)
        else:
            print('%s的课如下:' % self._name)
            for course in self._course_list:
               print(course.get_name(), end=' ')
            print()


class Teacher(People):
    def __init__(self, name):
        super().__init__(name)


class Student(People):
    def __init__(self, name):
        super().__init__(name)


if __name__ == '__main__':
    course1 = Course('cs231', 100)
    course2 = Course('cs232', 120)
    print(course1)
    print(course2)

    teacher1 = Teacher('laowang')
    teacher2 = Teacher('laoli')
    student1 = Student('xiaoxing')

    teacher1.add_course(course1)
    teacher1.add_course(course2)

    student1.add_course(course1)

    teacher1.print_course_data()
    teacher2.print_course_data()
    student1.print_course_data()