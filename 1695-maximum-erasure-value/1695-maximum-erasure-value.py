class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        r = 0
        res = 0
        curr_sum = 0

        while r<len(nums):
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l+=1
            seen.add(nums[r])
            curr_sum += nums[r]
            res = max(res, curr_sum)
            r+=1
        return res
            