class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        stack = []
        for i in nums:
            if i < pivot:
                stack.append(i)
        for i in nums:
            if i == pivot:
                stack.append(i)
        for i in nums:
            if i > pivot:
                stack.append(i)
        return stack
        
