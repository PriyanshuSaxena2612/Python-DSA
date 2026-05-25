class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        n = format(n, 'b')
        len_n = len(n)
        half_1 = (len(n)-1)//2
        return n[:half_1] == n[half_1:]
