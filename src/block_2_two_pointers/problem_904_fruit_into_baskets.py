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

        if size <= 2:
            return size

        result = 1
        ix = 0
        jy = 1
        changes = 0
        x = fruits[0]
        y = fruits[1]

        while jy < size:
            if fruits[jy] != fruits[jy - 1]:
                if y == x:
                    y = fruits[jy]
                changes += 1

                if fruits[jy] != x and fruits[jy] != y:
                    if jy - ix > result:
                        result = jy - ix

                    while changes > 1:
                        ix += 1
                        if fruits[ix] != fruits[ix - 1]:
                            changes -= 1

                    x = y
                    y = fruits[jy]

            jy += 1

        if jy - ix > result:
            result = jy - ix

        return result
