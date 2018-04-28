#    -*-    coding: utf-8    -*-
'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
import collections
class MovingAverage(object):
    def __init__(self, size):
        self.queue = collections.deque(maxlen = size)
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)
        """
        :type val: int
        :rtype: float
        """
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
