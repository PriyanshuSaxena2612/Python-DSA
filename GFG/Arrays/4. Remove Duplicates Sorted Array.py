# Question Link: https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        # first approach
        i = 0
        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i+=1
                arr[i] = arr[j]
        return arr[:i+1]
                
        
        # second approach
        arr_set = set()
        result = []
        for i in range(len(arr)):
            if arr[i] not in arr_set:
                result.append(arr[i])
                arr_set.add(arr[i])
        return result
