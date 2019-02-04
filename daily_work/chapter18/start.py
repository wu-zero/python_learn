import sys ,os
path = os.path.dirname(__file__)
sys.path.append(path)
from core import manager_src,student_src,teacher_src

if __name__ == '__main__':
    while True:
        print('''
                1、管理者
                2、老师
                3、学生
                q、退出
                ''')
        i = input("请选择:")
        if i == '1':
            manager_src.run()
        elif i == '2':
            teacher_src.run()
        elif i == '3':
            student_src.run()
        elif i == 'q':
            break
