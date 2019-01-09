# 2. 修改文件内容，把文件中的mac都替换成linux
with open('b.txt', 'rb') as read_f, open('b_new.txt', 'wb') as write_f:
    for line in read_f:
        write_f.write(line.replace('mac'.encode(), 'linux'.encode()))
