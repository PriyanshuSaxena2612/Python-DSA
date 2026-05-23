from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        k = len(p)
        if n < k:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:k])
        res = []

        for i in range(n - k):
            if s_count == p_count:
                res.append(i)
            trailing = s[i]
            leading = s[i + k]
            s_count[trailing] -= 1
            if s_count[trailing] == 0:
                del s_count[trailing]
            s_count[leading] += 1
        if s_count == p_count:
            res.append(n - k)

        return res
