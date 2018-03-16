'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''
# @param n, an integer
# @return an integer
class Solution:
    def reverseBits(self, n):
        s = bin(n)[2:]
        ret = '0b'
        i = 0
        while i<32:
            if i < len(s):
                ret += s[-i-1]
            else:
                ret += '0'
            i += 1
        return int(ret,2)

if __name__ == "__main__":
	sol = Solution()
	print(sol.reverseBits(int(raw_input("Enter the number: "))))
