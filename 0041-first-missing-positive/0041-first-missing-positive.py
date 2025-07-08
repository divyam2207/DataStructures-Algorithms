class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            ideal_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[ideal_idx]:
                nums[i], nums[ideal_idx] = nums[ideal_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        
        return n+1