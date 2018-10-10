# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     binary_search
   Description : 二分查找
   Author :       机器灵砍菜刀
   Init Date：          2018/10/10
-------------------------------------------------
"""

"""
时间复杂度：最优O(1) 最坏O（logn）
"""


# 递归版本
def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n == 0:
        return False
    else:
        mid = n // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binary_search(alist[:mid], item)
            else:
                return binary_search(alist[mid+1:], item)


# 非递归版本
def binary_search_second(alist, item):
    n = len(alist)
    first = 0
    last = n -1
    while first <= last:
        mid = (first + last) //2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [1,3,5,6,7,9,10]
    print(binary_search(li, 4))
    print(binary_search(li, 3))

    print(binary_search_second(li, 4))
    print(binary_search_second(li, 3))