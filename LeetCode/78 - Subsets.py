class Solution:
    def find_subsequence(self, nums, index, subset, result):
        if index == len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.find_subsequence(nums,index+1,subset,result)
        subset.pop()
        self.find_subsequence(nums,index+1,subset,result)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.find_subsequence(nums,0,[],result)
        return result
        