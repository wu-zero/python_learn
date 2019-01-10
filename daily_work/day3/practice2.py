# 1. 有列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，去重，得到新列表,且新列表无需保持列表原来的顺序
l = ['a', 'b', 1, 'a', 'a']
print(set(l))

# 2.在上题的基础上，保存列表原来的顺序
l = ['a', 'b', 1, 'a', 'a']
l_new = []
for i in l:
    if i not in l_new:
        l_new.append(i)
print(l_new)

# 3.去除文件中重复的行，肯定要保持文件内容的顺序不变(后面的章节会讲文件操作)
with open('data.txt','r') as read_f, open('data2.txt','w') as write_f:
    lines_new = []
    for line in read_f:
        if line not in lines_new:
            lines_new.append(line)
            write_f.write(line)

# 4.有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l = [{'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'albert','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},]

l_set = set()
l_new = []
for item in l:
    val = (item['name'], item['age'], item['sex'])
    if val not in l_set:
        l_set.add(val)
        l_new.append(item)
print(l_new)
