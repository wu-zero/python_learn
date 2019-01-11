# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表


# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
def file_data_replace(original_file_name,new_file_name,change_from,change_to):
    with open(original_file_name, 'r') as read_f, open(new_file_name, 'w') as write_f:
        for line in read_f:
            write_f.write(line.replace(change_from, change_to))

#
# if __name__ == '__main__':
#
#     file_name1 = 'a.txt'
#     file_name2 = 'a_new.txt'
#     change_from = 'mac'
#     change_to = 'linux'
#     file_data_replace(file_name1,file_name2,change_from,change_to)

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def count_str(str_data):
    int_count = 0
    letter_count = 0
    space_count = 0
    other_count = 0
    for i in str_data:
        if i.isdigit():
            int_count += 1
        elif i.isalnum():
            letter_count += 1
        elif i == ' ':
            space_count += 1
        else:
            other_count += 1
    return int_count, letter_count, space_count, other_count


# if __name__ == '__main__':
#     str_data = ' 1 + 1 = two'
#     print(str_data)
#     print('数字有%d个,字母有%d个,空格有%d个,其他有%d个。' % count_str(str_data))

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def if_longer_than_5(data):
    return len(data) > 5

# if __name__ == '__main__':
#     print(if_longer_than_5('sdfasdfasd'))
#     print(if_longer_than_5([2,2,2,2,2,]))
#     print(if_longer_than_5((2,2,2,2,22)))
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def make_length_become2_if_longer_than2(list_data):
    if len(list_data) > 2:
        return list_data[0:2]
    else:
        return list_data


# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def choose_odd_index(data):
    return data[1::2]

# if __name__ == '__main__':
#      print(choose_odd_index([0,1,2,3,4,5]))
#      print(choose_odd_index((0, 1, 2, 3, 4, 5)))

# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
def make_value_length_become2_if_longer_than2(dict_data):
    from copy import deepcopy
    dict_data = deepcopy(dict_data)
    for i_key, i_value in dict_data.items():
        dict_data[i_key] = make_length_become2_if_longer_than2(i_value)

    return dict_data

# if __name__ == '__main__':
#     dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
#     print(dic)
#     print(make_value_length_become2_if_longer_than2(dic))
