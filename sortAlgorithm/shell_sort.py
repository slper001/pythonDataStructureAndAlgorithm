# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     shell_sort
   Description : 希尔排序(插入排序的改进版)
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""
"""
最优时间复杂度：根据步长序列的不同而不同
最坏时间复杂度：O（n2）
稳定性：不稳定
"""


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2

    while gap > 0:  # gap变化到0之前, 插入算法执行的次数
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    shell_sort(alist=li)
    print(li)