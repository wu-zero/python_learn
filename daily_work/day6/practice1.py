menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '电子厂':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}



tag=True
while tag:
    menu1 = menu
    for key in menu1: # 打印第一层
        print(key)

    choice1=input('第一层>>: ').strip() # 选择第一层

    if choice1 == 'b': # 输入b，则返回上一级
        break
    if choice1 == 'q': # 输入q，则退出整体
        tag=False
        continue
    if choice1 not in menu1: # 输入内容不在menu1内，则继续输入
        continue

    while tag:
        menu_2=menu1[choice1] # 拿到choice1对应的一层字典
        for key in menu_2:
            print(key)

        choice2 = input('第二层>>: ').strip()

        if choice2 == 'b':
            break
        if choice2 == 'q':
            tag = False
            continue
        if choice2 not in menu_2:
            continue

        while tag:
            menu_3=menu_2[choice2]
            for key in menu_3:
                print(key)

            choice3 = input('第三层>>: ').strip()
            if choice3 == 'b':
                break
            if choice3 == 'q':
                tag = False
                continue
            if choice3 not in menu_3:
                continue

            while tag:
                menu_4=menu_3[choice3]
                for key in menu_4:
                    print(key)

                choice4 = input('第四层>>: ').strip()
                if choice4 == 'b':
                    break
                if choice4 == 'q':
                    tag = False
                    continue
                if choice4 not in menu_4:
                    continue
