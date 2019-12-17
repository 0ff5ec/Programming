class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i
        time = 0
        init = 0
        for letter in word:
            time += abs(d[letter] - init)
            init = d[letter]
        return time

