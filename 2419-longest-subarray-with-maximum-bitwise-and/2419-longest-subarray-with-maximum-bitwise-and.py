class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = res = 0
        max_ele = max(nums)
        for each in nums:
            if each == max_ele:
                res += 1
            else:
                res = 0
            
            ans = max(ans, res)

        return ans
