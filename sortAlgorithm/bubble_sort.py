# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     bubble_sort
   Description : 冒泡排序
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""

"""
时间复杂度：
最优：O(n)：表示遍历一次发现没有任何可以交换的元素，排序结束。
最坏：O(n2)
稳定
"""


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    # for i in range(0, n-1):
    #     for j in range(0, n-1-i):
    #         if alist[j] > alist[j+1]:
    #             alist[j], alist[j+1] = alist[j+1], alist[j]

    for i in range(n-1, 0, -1):  # i代表每轮步数
        count = 0
        for j in range(i):  # j代表一轮中的移动
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:  # 交换次数为0代表如果有序，就不用继续了
            return


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    bubble_sort(alist=li)
    print(li)