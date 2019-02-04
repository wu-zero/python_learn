
class Course:
    def __init__(self, name='', price=0, cycle=0):
        self.__name = name
        self.__price = price
        self.__weeks = cycle
        self.__group_dict = {}

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def weeks(self):
        return self.__weeks

    @property
    def group_list(self):
        return list(self.__group_dict.keys())

    def add_group(self, group):
        if group.name in self.__group_dict:
            return False, "班级已存在"
        else:
            self.__group_dict[group.name] = group
            return True, "班级添加成功"

    def get_group_from_name(self, group_name):
        if group_name in self.__group_dict:
            return self.__group_dict[group_name]
        else:
            return None

    def __str__(self):
        return "课程:%s,价格:%s,周期:%s\n包含班级:%s" % (self.name, self.price, self.weeks, ','.join(self.group_list))

    def show(self):
        print(self)
        print("班级信息:")
        if self.__group_dict is None:
            print("暂无班级")
        for group_name, group in self.__group_dict.items():
            print(group)

    @classmethod
    def create(cls):
        course_name = input("课程名称:")
        course_price = int(input("课程价格:"))
        course_cycle = int(input("课程周期:"))
        course = Course(course_name, course_price, course_cycle)
        return course


if __name__ == '__main__':
    course1 = Course('Python', 12, 12)

    from lib.Group import Group
    group1 = Group('一班')
    group2 = Group('二班')
    print(course1.add_group(group1))
    print(course1.add_group(group2))
    print(course1)
    course1.show()
