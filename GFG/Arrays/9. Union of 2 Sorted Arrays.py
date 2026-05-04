class Solution:
    def findUnion(self, a, b):
      # first method
      a[:] = a + b
      return sorted(list(set(a)))
      # second method
        n1 = len(a)
        n2 = len(b)
        i, j = 0, 0
        res = []
        while i < n1 and j < n2:
            if a[i] == b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        while i < n1:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        while j < n2:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        return res
