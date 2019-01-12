# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
# albert male 18 3000
# james male 38 30000
# 林志玲 female 28 20000
# 新垣结衣 female 28 10000
#
# 要求:
# 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'albert','sex':'male','age':18,'salary':3000}的形式
#
# 2 根据1得到的列表,取出薪资最高的人的信息
# 3 根据1得到的列表,取出最年轻的人的信息
# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# 5 根据1得到的列表,过滤掉名字以a开头的人的信息
# 6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值

# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
# albert male 18 3000
# james male 38 30000
# 林志玲 female 28 20000
# 新垣结衣 female 28 10000
#
# 要求:
# 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'albert','sex':'male','age':18,'salary':3000}的形式

with open('a.txt', encoding='utf-8') as f:
    items = (line.split() for line in f)
    info = [{'name': name, 'sex': sex, 'age': age, 'salary': salary} \
            for name, sex, age, salary in items]

print(info)

# 2 根据1得到的列表,取出薪资最高的人的信息
print(max(info, key=lambda dic: dic['salary']))

# 3 根据1得到的列表,取出最年轻的人的信息
print(min(info, key=lambda dic: dic['age']))

# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
info_new = map(lambda item: {'name': item['name'].capitalize(),
                             'sex': item['sex'],
                             'age': item['age'],
                             'salary': item['salary']}, info)

print(list(info_new))

# 5 根据1得到的列表, 过滤掉名字以a开头的人的信息
g = filter(lambda item: item['name'].startswith('a'), info)
print(list(g))


# 6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
def fib(a, b, stop):
    if a > stop:
        return
    print(a, end=' ')
    fib(b, a + b, stop)


fib(0, 1, 10)

# 7 一个嵌套很多层的列表，如l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]，用递归取出所有的值
l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]


def get(seq):
    for item in seq:
        if type(item) is list:
            get(item)
        else:
            print(item)


get(l)
