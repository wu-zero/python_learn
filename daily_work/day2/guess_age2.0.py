# 猜年龄
Age = 15
Count_Max = 3

print('游戏开始')
count = 0
while count < Count_Max:
    count += 1
    input_age = int(input('输入您猜的年龄:\n'))
    if input_age < Age:
        print('猜小了，请重试')
    elif input_age > Age:
        print('猜大了，请重试')
    else:
        print('猜对了！')
        break
    if count == Count_Max:
        input_continue_flag = input('是否继续？是(Y or y) 否(N or n)\n')
        if input_continue_flag in ['Y', 'y']:
            count = 0
        elif input_continue_flag in ['N', 'n']:
            print('您已放弃！')
else:
    print('没有猜出，游戏结束。。')
