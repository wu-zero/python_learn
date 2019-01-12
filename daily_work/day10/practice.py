# 1、将names=['albert','james','kobe','kd']中的名字全部变大写
# 2、将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
# 3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# 4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
# 5、思考题
# with open('a.txt') as f:
#     g=(len(line) for line in f)
# print(sum(g)) #为何报错？
# 6、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# （1）求总共花了多少钱？
# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# （3）求单价大于10000的商品信息,格式同上

# 1、将names=['albert','james','kobe','kd']中的名字全部变大写
names = ['albert', 'james', 'kobe', 'kd']
names_new = [name.upper() for name in names]
print(names, names_new)
print('='*50)


# 2、将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names=['albert','jr_shenjing','kobe','kd']
names_new = [len(name) for name in names if not name.endswith('shenjing')]
print(names, names_new)
print('='*50)


# 3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
with open('a.txt',encoding='utf-8') as f:
    print(max(len(line) for line in f))
print('='*50)

# 4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
with open('a.txt', encoding='utf-8') as f:
    print(sum(len(line) for line in f))
    print(sum(len(line) for line in f))  # 求包换换行符在内的文件所有的字符数，为何得到的值为0?
    print(sum(len(line) for line in f))  # 求包换换行符在内的文件所有的字符数，为何得到的值为0?
    # 文件指针在文件末尾，so
    # 添加f.seek(0, 0)就ok了
    # 即
    # f.seek(0, 0)
    # print(sum(len(line) for line in f))
print('='*50)

# 5、思考题
# with open('a.txt') as f:
#     g=(len(line) for line in f)
# print(sum(g)) #为何报错？

# 处理了已经被关闭的数据，g数据在with内部，处理它应该放在with内部


#6、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# （1）求总共花了多少钱？
# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# （3）求单价大于10000的商品信息,格式同上

# （1）求总共花了多少钱？
with open('shopping.txt', encoding='utf-8') as f:
    info = [line.split(',') for line in f]
    cost = sum(float(price) * int(count) for _, price, count in info)
    print(cost)

# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
with open('shopping.txt', encoding='utf-8') as f:
    info = [{
        'name': line.split(',')[0],
        'price': float(line.split(',')[1]),
        'count': int(line.split(',')[2]),
    } for line in f]
    print(info)

# （3）求单价大于10000的商品信息,格式同上
with open('shopping.txt', encoding='utf-8') as f:
    info=[{
        'name': line.split(',')[0],
        'price': float(line.split(',')[1]),
        'count': int(line.split(',')[2]),
    } for line in f if float(line.split(',')[1]) > 10000]
    print(info)
