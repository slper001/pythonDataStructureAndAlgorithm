# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     select_sort
   Description : 选择排序
   Author :       机器灵砍菜刀
   Init Date：          2018/10/9
-------------------------------------------------
"""
"""
时间复杂度：
最坏与最优O(n2)
稳定性：不稳定（考虑升序每次选择最大的情况）
"""


def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for i in range(n-1):  # 0到n-2
        min_value_index = i
        for j in range(i+1, n):  # 找到后面的最小值
            if alist[min_value_index] > alist[j]:
                min_value_index = j
        alist[i], alist[min_value_index] = alist[min_value_index], alist[i]  # 将最小值置于i的位置


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    select_sort(alist=li)
    print(li)
