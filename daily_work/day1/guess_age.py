# 猜年龄
Age = 15
Count_Max = 5

print('游戏开始')
count = 0
while count < Count_Max:
    input_age = int(input('输入您猜的年龄:\n'))
    if input_age < Age:
        print('猜小了，请重试')
    elif input_age > Age:
        print('猜大了，请重试')
    else:
        print('猜对了！')
        break

    count += 1
else:
    print('没有猜出，游戏结束。。')
