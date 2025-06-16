class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        start = nums[0]
        res = -1

        for i in range(1, len(nums)):
            if nums[i] <= start:
                start = nums[i]
            else:
                res = max(res, nums[i]-start)
        
        return res