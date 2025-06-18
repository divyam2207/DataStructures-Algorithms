class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i<len(nums)-2:
            if nums[i+2] - nums[i] <= k:
                res.append([nums[i], nums[i+1], nums[i+2]])
                i+=2
            else:
                return []
            i+=1
        
        return res