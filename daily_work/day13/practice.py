# 1. 什么是面向对象编程
# 2. 所有程序都因该使用面向对象来设计吗?为什么?
# 3. 什么是对象 什么是类
# 4. 在面向过程编程中我们思考解决方案时,是分析完成任务时需要哪些步骤,按照什么样的顺序来编写,而在面向对象编程中我们从操作者转变为指挥者 首先思考的是什么?
# 5. 一个类中通常包含变量和函数,它们分别用于描述什么?
# 6. 类在定义阶段发生了什么
# 7. 创建对象时发生了什么
# 8. 程序设计：(如果写不出来就往后面看一章)      学生成绩管理系统
#   1.根据姓名查看学生所有成绩
#   2.查看所有人的某学科成绩
#   3.查看总平均分
#   4.查看某人的某学科成绩
#   5.根据姓名删除学生信息增强版要求(选做)
#       1.首先编写json格式的数据文件 内容为学生
#       2.将json数据解析后转换为学生对象在进行增删改查


class Student:
    def __init__(self,id,name,chinese_score=0,english_score=0,math_score=0):
        self._id = id
        self._name = name
        self._chinese_score = chinese_score
        self._english_score = english_score
        self._math_score = math_score

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_chinese_score(self):
        return self._chinese_score

    def get_englisth_score(self):
        return self._english_score

    def get_math_score(self):
        return self._math_score

    def show_score(self):
        print('%s的成绩如下:语文%3d;数学%3d;英语%3d' % (self._name, self._chinese_score, self._english_score, self._math_score))

    def show_one_score(self, subject):
        if subject == 'chinese':
            print('%s的%s成绩如下:%3d' % (self._name, subject, self.get_chinese_score()))
        elif subject == 'english':
            print('%s的%s成绩如下:%3d' % (self._name, subject, self.get_englisth_score()))
        elif subject == 'math':
            print('%s的%s成绩如下:%3d' % (self._name, subject, self.get_math_score()))


class Class:
    def __init__(self):
        self._student_list = []
        self._student_number = 0

    # def find_student_through_id(self, id):
    #     for student in self._student_list:
    #         if student.get_id() == id:
    #             return student
    #     return None

    def find_student_through_name(self, name):
        for student in self._student_list:
            if student.get_name() == name:
                return student
        return None

    def add_student(self,id,name,chinese_score=0,english_score=0,math_score=0):
        stu = Student(id,name,chinese_score,english_score,math_score)
        self._student_list.append(stu)
        self._student_number += 1

    def show_one_student_all_score(self, name):
        stu = self.find_student_through_name(name)
        if stu is not None:
            stu.show_score()

    def show_one_student_one_score(self, name, subject):
        stu = self.find_student_through_name(name)
        if stu is not None:
            stu.show_one_score(subject)

    def show_all_student_all_score(self):
        for stu in self._student_list:
            stu.show_score()

    def show_all_student_one_score(self, subject):
        for stu in self._student_list:
            stu.show_one_score(subject)


class1 = Class()
# 添加学生
class1.add_student(1,'xm',99,100,100)
class1.add_student(2,'xg',93,56,68)
class1.add_student(3,'xh',100,88,77)

print('显示所有人成绩')
class1.show_all_student_all_score()
print('='*40)

print('显示一个人成绩')
class1.show_one_student_all_score('xh')
print('='*40)

print('显示某一科目成绩')
class1.show_all_student_one_score('chinese')
print('='*40)

print('显示某人某一科目成绩')
class1.show_one_student_one_score('xm','english')
print('='*40)

