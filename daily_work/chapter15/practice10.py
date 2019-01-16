# 10. 如下示例, 在没有学习类这个概念时,数据与功能是分离的,请用面向对象的形式优化以下代码
# def exc1(host,port,db,charset):
#     conn=connect(host,port,db,charset)
#     conn.execute(sql)
#     return xxx
# def exc2(host,port,db,charset,proc_name):
#     conn=connect(host,port,db,charset)
#     conn.call_proc(sql)
#     return xxx
# # 每次调用都需要重复传入一堆参数
# exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
# exc2(‘127.0.0.1’,3306,'db1','utf8','存储过程的名字')

# 优化如下：
# class MyConn:
#     def __init__(self,host,port,db,charset,sql):
#         self._conn = connect(host,port,db,charset)
#         self._sql = sql
#
#     def exc1(self):
#         self._conn.execute(self._sql)
#         return xxx
#
#     def exc2(self,proc_name):
#         self._conn.call_proc(self._sql)
#         return xxx
#
# myconn = MyConn('127.0.0.1',3306,'db1','utf8',sql)
# myconn.exc1()
# myconn.exc2('存储过程的名字')