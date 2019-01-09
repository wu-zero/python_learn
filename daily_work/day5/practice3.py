# 1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数

price_all = 0
with open('a.txt', 'rb') as f:
    for line in f:
        line_split = line.split()
        price, num = int(line_split[1]), int(line_split[2])
        price_all += price * num
print(price_all)