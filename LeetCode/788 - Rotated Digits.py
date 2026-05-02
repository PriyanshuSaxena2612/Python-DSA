class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            s = str(i)
            if any(char in '347' for char in s):
                continue
            if any(char in '2569' for char in s):
                count+=1
        return count
