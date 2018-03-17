'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
"""
        :type n: int
        :rtype: int
        """
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        if high == low and isBadVersion(high):
            return 1
        mid = (high + low)//2
        while high > low:
            if isBadVersion(mid):
                high = mid
            elif not isBadVersion(mid):
                low = mid
            if high == low + 1:
                return low if isBadVersion(low) else high
            mid = (high+low)//2
        return mid if isBadVersion(mid) else high
