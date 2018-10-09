# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     study_timeit
   Description :  代码执行时间测量模块timeit
   Author :       机器灵砍菜刀
   Init Date：          2018/10/8
-------------------------------------------------
"""
"""
timeit模块可以用来测试一小段Python代码的执行速度
class timeit.Timer(stmt='pass',setup='pass',timer=<timer function>)
Timer是测量小段代码执行速度的类
stmt参数是要测试的代码语句(statment)
setup参数时运行代码时需要的设置
timer参数时一个定时器函数,与平台有关
timeit.Timer.timeit(number=1000000)
Timer类中测试语句执行舒服的对象方法.number参数是测试代码时的测试次数,默认为1000000次
方法返回执行代码的平均耗时,一个float类型的秒数
"""

from timeit import Timer


def t1():
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    li = []
    for i in range(10000):
        li += [i]


def t3():
    li = [i for i in range(10000)]


def t4():
    li = list(range(10000))


def t5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = Timer('t1()', 'from __main__ import t1')
print('append:', timer1.timeit(1000))

timer2 = Timer('t2()', 'from __main__ import t2')
print('+:', timer2.timeit(1000))

timer3 = Timer('t3()', 'from __main__ import t3')
print('[i for in range]', timer3.timeit(1000))

timer4 = Timer('t4()', 'from __main__ import t4')
print('list(range()):', timer4.timeit(1000))

timer5 = Timer('t5()', 'from __main__ import t5')
print('extend:', timer5.timeit(1000))


def t6():
    li = []
    for i in range(10000):
        li.append(i)


def t7():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer6 = Timer('t6()', 'from __main__ import t6')
print('head:', timer6.timeit(1000))

timer7 = Timer('t7()', 'from __main__ import t7')
print('tail:', timer7.timeit(1000))

