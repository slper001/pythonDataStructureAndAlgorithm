# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     merge_sort
   Description : 归并排序
   Author :       机器灵砍菜刀
   Init Date：          2018/10/10
-------------------------------------------------
"""
"""
时间复杂度：
最优最坏均是O(nlogn)
稳定
"""


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # left代表左边经过归并排序形成的有序子序列
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    #  将两个子序列合并形成一个整体
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer +=1
        else:
            result.append(right[right_pointer])
            right_pointer +=1

    result += left[left_pointer:]
    result += right[right_pointer:]

    return result


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    print(merge_sort(li))