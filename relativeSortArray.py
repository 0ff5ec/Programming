class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in arr1:
            if d.get(i) is None:
                d[i] = 1
            else:
                d[i] += 1
        res = []
        for i in arr2:
            if d.get(i):
                res += [i]*d[i]
                del d[i]
        res1 = []
        for k, v in d.items():
            res1 += [k]*v
        return res + sorted(res1)
