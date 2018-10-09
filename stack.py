# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     stack
   Description : 栈
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈"""
        self.__list.append(item)

    def pop(self):
        """弹栈"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(4)
    s.push(5)
    print(s.pop())
