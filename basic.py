#encoding:utf-8
'''
key word:
pass,break,continue,return,
while for if elif else
and not or
try except finally raise
from  x import b ,import x as b
with x as c:
yield ,lambda
in ,is ,
global,class,print,def,del

collections  and functions:
dict,tupple,list,String,Numbers
list,tupple,set,dict,int,long,float,complex,str,repr,eval

运算符：
算术，关系，逻辑，条件，赋值，位，成员（in,is）

for else:while else:if elfi,else,break,continue,return,pass

time,calendar,datetime,dateutil,pytz

os,file,
'''
a=12
b="12"
# c=chr(64)
c='c'
# print("{a},{b},{c}".format(a=a,b=b,c=c))
# print("{0},{1},{2}".format(a,b,c))
# print("%d,%s,%c" % (a,b,c))

'''
import datetime
import time
dt=datetime.date.today()
print(dt)
st=dt.strftime("%Y%m%d")
print(st)
st=time.strptime("2016-10-11 12:12:30","%Y-%m-%d %H:%M:%S")
print(st)
'''

import copy
b=[[9,12,12,123],[123,234,234]]
a=copy.copy(b)
# a=copy.deepcopy(b)
a.append(1444)
# print(a)
# a=23
# print(a)
# print(b)
# print(id(a))
# print(id(b))


import  numpy as np
import scipy as sp
arr=np.array([1,2,2])
print(arr.ndim)
print(arr.shape)