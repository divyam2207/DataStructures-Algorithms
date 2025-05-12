class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for each in nums:
            digits = 1
            while each:
                each //= 10
                digits ^= 1
            if digits == 1:
                res += 1
        
        return res

