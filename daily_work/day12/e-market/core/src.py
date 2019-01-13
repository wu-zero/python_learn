from conf import settings
from lib import common
import time

logger = common.get_logger(__name__)

current_user = {'user': None, 'login_time': None, 'timeout': int(settings.LOGIN_TIMEOUT)}







def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['user']:
            interval = time.time() - current_user['login_time']
            if interval < current_user['timeout']:
                return func(*args, **kwargs)
        name = input('name>>: ')

        db = common.conn_db()
        if db.get(name):  # 登录

            if db.get(name).get('locked') == 1:
                logger.warning('您被锁定了')
                print('您被锁定了')
            else:
                user_login_error_time = 0

                while True:
                    if user_login_error_time >= 3:
                        logger.warning('错误3次，您被锁定了')
                        print('错误3次，您被锁定了')
                        db[name]['locked'] = 1
                        common.save_db(db)
                        break
                    password = input('password>>: ')
                    if password == db.get(name).get('password'):
                        logger.info('登录成功')
                        print('登录成功')
                        current_user['user'] = name
                        current_user['login_time'] = time.time()
                        return func(*args, **kwargs)
                    else:
                        logger.warning('密码错误')
                        user_login_error_time += 1

        else:  # 注册
            register_flag = input('用户名不存在，是否注册? 是(Y or y) 否(others)\n')
            if register_flag in ['Y', 'y']:
                password = input('password>>: ')
                db[name] = {"password": password, "money": 0}
                logger.info('登录成功')
                print('登录成功')
                current_user['user'] = name
                current_user['login_time'] = time.time()
                common.save_db(db)
                return func(*args, **kwargs)
            else:
                logger.info('用户名不存在,且拒绝注册')

    return wrapper


@auth
def buy():
    db = common.conn_db()
    money = db.get(current_user['user']).get('money')
    print('你有%d元' %money)
    goods_dict = {'apple': 1,
                  'banana': 1
                  }
    print(goods_dict.keys())
    goods_bought_dic = {}
    while True:
        input_str = input('buy goods(such as apple) number(such 5)  ')
        input_str_split = input_str.split(' ')
        if len(input_str_split) == 1 and input_str_split[0] == 'q':
            db[current_user['user']]['money'] = money
            common.save_db(db)
            print('退出购物，你买了：')
            print(goods_bought_dic)
            print('你还有%d元' % money)
            break
        elif len(input_str_split) == 3:
            goods, number = input_str_split[1], input_str_split[2]
            if goods in goods_dict:
                goods_price = goods_dict[input_str_split[1]] * int(input_str_split[2])
                if goods_price <= money:
                    money -= goods_price
                    print('买成功，你还有%d' % (money))
                    if goods in goods_bought_dic:
                        goods_bought_dic[goods] += number
                    else:
                        goods_bought_dic[goods] = number
                else:
                    print('你没有足够的钱')

@auth
def withdraw_money():
    db = common.conn_db()
    money = db.get(current_user['user']).get('money')
    print('你有%d元' % money)
    withdraw_money_count = int(input('取多少钱？ '))
    if withdraw_money_count <= money:
        money -= withdraw_money_count
        db[current_user['user']]['money'] = money
        common.save_db(db)
        print('取成功，你还有%d' % (money))
    else:
        print('你没有足够的钱')


@auth
def deposit_money():
    db = common.conn_db()
    money = db.get(current_user['user']).get('money')
    print('你有%d元' % money)
    deposit_money_count = int(input('存多少钱？ '))
    money += deposit_money_count
    db[current_user['user']]['money'] = money
    common.save_db(db)
    print('存成功，你还有%d' % (money))


@auth
def run():

    while True:
        print('''
操作：
    1 购物
    2 取钱
    3 存钱
    q 退出
    ''')
        choice = input('>>: ').strip()
        if not choice: continue
        if choice == '1':
            buy()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == 'q':
            break
