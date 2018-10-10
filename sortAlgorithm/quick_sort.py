# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     quick_sort
   Description : 快排
   Author :       机器灵砍菜刀
   Init Date：          2018/10/10
-------------------------------------------------
"""

"""
最优时间复杂度O(nlogn)
最坏时间复杂度：O(n2)
稳定性：不稳定
"""


def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环中退出时，low==high
    alist[low] = mid_value

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low-1)

    # 对low右边的列表排序
    quick_sort(alist, low+1, last)


# 最简洁快速排序
def quicksort(array):
    less, greater = [], []
    if len(array) <=1:
        return array
    pivot = array.pop()
    for x in array:
        if x<= pivot: less.append(x)
        else:greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    li = [3,5,6,2,4,23,5,232,6,2,1,4,5,32,34]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)

    print("")

    li2 = [3, 5, 6, 2, 4, 23, 5, 232, 6, 2, 1, 4, 5, 32, 34]
    print(li2)
    print(quicksort(li2))

