class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count =Counter(nums)
        res = 0
        
        for each in nums:
            if each+1 in count:
                res = max(res, count[each]+count[each+1])
        
        return res