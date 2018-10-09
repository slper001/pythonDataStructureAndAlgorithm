# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     queue
   Description : 队列
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""


class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        return self.__list.pop()

    def is_empty(self):
        """判断空"""
        return self.__list == []

    def size(self):
        """队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    d = Queue()
    d.enqueue(1)
    d.enqueue(4)
    d.enqueue(6)
    print(d.dequeue())
    print(d.dequeue())
