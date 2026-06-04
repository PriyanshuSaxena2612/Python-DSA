class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2+1):
            s = str(i)
            if len(s) <= 2:
                continue
            else:
                for x in range(1,len(s)-1):
                    if s[x] > s[x-1] and s[x] > s[x+1]:
                        count += 1
                    elif s[x] < s[x-1] and s[x] < s[x+1]:
                        count += 1
        return count
