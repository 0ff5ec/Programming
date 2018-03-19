# -*- coding: utf-8 -*-
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
"""
        :type n: int
        :rtype: List[str]
        """
class Solution(object):
    def fizzBuzz(self, n):
        i = 1
        array = []
        while i < n+1:
            s = ""
            if i%15 == 0:
                s += "FizzBuzz"
            elif i%3 == 0:
                s += "Fizz"
            elif i%5 == 0:
                s += "Buzz"
            else:
                s = str(i)
            array.append(s)
            i += 1
        return array

if __name__ == "__main__":
	sol = Solution()
	print(sol.fizzBuzz(int(raw_input('Enter the number: '))))
