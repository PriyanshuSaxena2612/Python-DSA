class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n, start = 0, 0, 0
        while m < len(haystack) and n < len(needle):
            if needle[n] == haystack[m]:
                m += 1
                n += 1
                if n == len(needle):
                    return start
            else:
                n = 0
                start += 1
                m = start
        return -1
