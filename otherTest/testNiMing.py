import random
import time
import datetime
# print(random.random())#随机获取一个在0-1之间的浮点数，是隐藏的random.Random类的bai实例的random方法
# print(random.Random())#生成random模块里得Random类的一个实例，这个实例不会和其他Random实例共享状态，一般是在多线程的情况下使用。
# print(random.choice([1,3,2,4,2,1,3]))#从列表中随意获取一个元素
#生成一个4位小数的随机列表
# print([round(random.random(),4) for i in range(10)])
# myList = [9,2,3,4,5]
# print(random.choices(myList,k=5))
# print(random.choices(myList,cum_weights=[1,3,6,10,15],k=5))
# print(random.choices(myList,weights=[1,2,3,4,5],k=5))
# a = [1,4,2,6,3]
# print(random.choices(a,weights=[0,0,1,0,0],k=5))
# print(random.randrange(1,4))
# print(random.randint(1,3))
# print(random.uniform(1,2))
# print(random.sample(a,3))
# random.shuffle(a)
# print(a)

# print(time.time())
# print(time.localtime())
# print(time.localtime(time.time()))

# coding:utf-8
#导入读取Excel的库
import xlrd
#导入需要读取Excel表格的路径
data = xlrd.open_workbook(r'E:\test.xlsx')
table = data.sheets()[0]
y=''
#将列的值存入字符串
y=table.col_values(2)#读取列的值
#导入pyechats库
# from pyecharts import Bar
from pyecharts.charts import Bar
import numpy as np
t=np.linspace(1,296,len(y))#等间隔取值
bar=Bar("文章阅读量展示")#主副标题
bar.add("博客文章阅读量折线图展示",t,y,is_more_utils=True)#标题
bar.show_config()#展示HTML源代码
bar.render(r"C:/Users/ASUS/Desktop/txt1/bokezhexiantu.html")#保存到本地bokezhexiantu.html
