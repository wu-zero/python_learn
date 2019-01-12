# day7
#### 1. 将```names=['albert','james','kobe','kd']```中的名字全部变大写
见代码

#### 2. 将```names=['albert','jr_shenjing','kobe','kd']```中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
见代码
#### 3. 求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
见代码
#### 4. 求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
见代码
#### 5、思考题
```python
with open('a.txt') as f:
    g=(len(line) for line in f)
print(sum(g)) #为何报错？
```

#### 6. 文件```shopping.txt```内容如下
```
mac,20000,3
lenovo,3000,10
tesla,1000000,10
chicken,200,1
```
##### 1.求总共花了多少钱？
##### 2.打印出所有商品的信息，格式为```[{'name':'xxx','price':333,'count':3},...]```
##### 2.求单价大于10000的商品信息,格式同上
