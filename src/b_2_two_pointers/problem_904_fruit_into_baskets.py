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
