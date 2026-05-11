"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

* `1 <= fruits.length <= 10^5`
* `0<= fruits[i] < fruits.length`
"""
from typing import List

from pygments.lexers import j


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        size = len(fruits)

        ix = 0
        jy = 0

        x = fruits[0]
        y = fruits[0]

        while jy < size - 1 and y == x:
            jy += 1
            y = fruits[jy]

        kz = jy + 1
        result = kz - ix

        while kz < size:
            z = fruits[kz]
            if z != fruits[jy]:
                if z != x and z != y:
                    if kz - ix > result:
                        result = kz - ix
                    ix = jy
                    jy = kz
                    x = fruits[ix]
                    y = fruits[jy]
                else:
                    jy = kz

            kz += 1

        if kz - ix > result:
            result = kz - ix

        return result
