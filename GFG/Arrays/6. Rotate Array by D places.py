class Solution:
    def reverseArr(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr
    def rotateArr(self, arr, d):
        #code here
        n = len(arr)
        d %= n
        # first approach
        arr[:] = arr[d:] + arr[:d]
        return arr
        # # second approach
        self.reverseArr(arr, 0, d-1)
        self.reverseArr(arr, d, n-1)
        self.reverseArr(arr, 0, n-1)
        return arr
        # third approach
        arr[0:d] = arr[0:d][::-1]
        arr[d:n] = arr[d:n][::-1]
        arr[:] = arr[::-1]
        return arr
