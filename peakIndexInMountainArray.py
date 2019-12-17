class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A[0] > A[1]:
            return 0
        if A[-1] > A[-2]:
            return len(A) - 1
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return i
