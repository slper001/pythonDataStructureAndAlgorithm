# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     insert_sort
   Description : 插入算法
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""
"""
时间复杂度
最优：O（n） 升序排列，序列已经处于升序状态
最坏：O（n2）
稳定性：稳定
"""


def insert_sort(alist):
    """插入算法"""
    n = len(alist)
    for i in range(1, n): # 分别拿1到n-1位置的数据进行插入 注:已经插入的数据是有序的
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    insert_sort(alist=li)
    print(li)