#    -*-    coding: utf-8    -*-
'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''
"""
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
from fractions import gcd
class Solution(object):
    def canMeasureWater(self, x, y, z):
        if x+y < z: return False
        elif x == z or y == z or x+y == z: return True
        else: return z%gcd(x,y) == 0

if __name__ == "__main__":
	sol = Solution()
	print(sol.canMeasureWater(int(raw_input('Enter x: ')),int(raw_input('Enter y: ')),int(raw_input('Enter z: '))))
