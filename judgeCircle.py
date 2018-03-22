# -*- coding: utf-8 -*-
'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''
"""
        :type moves: str
        :rtype: bool
        """
class Solution(object):
    def judgeCircle(self, moves):
        xMoves = 0
        yMoves = 0
        for letter in moves:
            if letter == "U":
                yMoves += 1
            elif letter == "D":
                yMoves -= 1
            elif letter == "R":
                xMoves += 1
            elif letter == "L":
                xMoves -= 1
        if xMoves == 0 and yMoves == 0:
            return True
        else:
            return False

if __name__ == "__main__":
	sol = Solution()
	print(sol.judgeCircle(raw_input('Enter your moves: ')))
