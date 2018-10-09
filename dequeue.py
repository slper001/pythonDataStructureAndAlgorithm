# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     dequeue
   Description : 双端队列
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""


class Dequeue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部入队"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部入队"""
        return self.__list.append(item)

    def pop_front(self):
        """头部出队"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部出队"""
        return self.__list.pop()

    def is_empty(self):
        """判断空"""
        return self.__list == []

    def size(self):
        """队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    d = Dequeue()