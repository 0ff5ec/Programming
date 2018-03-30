#   -*-   coding: utf-8   -*-
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack(object):

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append({'val':x,'min':x})
        else:
            self.stack.append({'val':x, 'min': min(x,self.getMin())})
        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        self.stack.pop()
        """
        :rtype: void
        """
        

    def top(self):
        return self.stack[-1]['val']
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.stack[-1]['min']
        """
        :rtype: int
        """
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
