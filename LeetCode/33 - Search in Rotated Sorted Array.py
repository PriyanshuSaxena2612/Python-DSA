class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j = 0,n-1
        while i<=j:
            mid=(i+j)//2
            # check if mid index is the target
            if target==nums[mid]:
                return mid
            # check if the left array is sorted
            if nums[i]<=nums[mid]:
                # check if target is in the left sorted array
                if target>=nums[i] and target<nums[mid]:
                    j=mid-1
                # else check in the second half
                else:
                    i=mid+1
            # else the right half is sorted
            else:
                if target<=nums[j] and target>nums[mid]:
                    i=mid+1
                # else check in the second half
                else:
                    j=mid-1
        return -1
