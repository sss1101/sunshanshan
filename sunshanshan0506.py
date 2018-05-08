# -*- coding:utf8 -*-
#使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断.
try:
    f=open('123','r')
except IOError:
    print ('无此文件')
finally:
    print ('不中断继续执行')

#用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
#
# def raise_f():
#定义一个函数，传入一个由小值数字组成列表，返回最大最小值
def mm(*l):
    print (max(l),min(l))
mm(1,2,3,5)
# 定义匿名函数，返回两数乘积
pro= lambda x,y:x*y
print(pro(2,3))

# 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def fun(*b):
    print(b)
fun([1,2,3])
# 写一个函数，返回N的阶乘
def jiecheng(n):
    if n==0 or n==1:
        return 1
    total=1
    for i in range(2,n+1):
        total*=i
    return total
print jiecheng(2)
#位置参数
def fun(name,age):
    print ("%s的年龄是%d" % (name,age))
fun("sun",18)

#默认参数
def fun(name,score=90):
    print ("%s的成绩是%d" % (name,score))
fun("sun",60)


# Try ...except... 如果执行出错，后续代码就不会执行。
try:
    f=open('文件','r')
except IOError:
    print ('无此文件')

# Try ...except...finally 不论是否发生异常，都执行finally中的语句。
try:
    f=open('123','r')

except IOError:
    print ('无此文件')
finally:
    print ('不中断继续执行')
# Try...except...else 不发生异常时，就执行else中的语句。
try:
    aa=22
    print (aa)
except IOError as ne:
    print (ne)
else:
    print ("没有异常才出现")

# NameError尝试访问一个未申明的变量
name='sunshanshan'
print (na)
# ZeroDivisinError除数为零
i=1/0
print (i)
# SyntaxError解释器语法错误
# KeyError请求一个不存在的字典关键字
# IndexError请求的索引超出序列范围
# FileNotFoundError文件不存在
s=open("aa",'r')

# AttributeError 尝试访问未知的对象属性


