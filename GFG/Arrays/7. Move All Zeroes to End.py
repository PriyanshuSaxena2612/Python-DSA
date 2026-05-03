# Question Link: https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	n = len(arr)
    	i, j = 0, 1
    	while j < n:
    	    if arr[i] == 0 and arr[j] != 0:
    	        arr[i], arr[j] = arr[j], arr[i]
    	        i += 1
    	        j += 1
            elif arr[i] == 0 and arr[j] == 0Just :
    	       j += 1
            else:
               i += 1
               j += 1
    	return arr
