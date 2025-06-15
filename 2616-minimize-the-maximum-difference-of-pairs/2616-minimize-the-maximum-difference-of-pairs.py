class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def search(diff)-> bool:
            res = 0
            i = 0
            while i <len(nums)-1:
                if abs(nums[i] - nums[i+1]) <= diff:
                    res += 1
                    i += 1
                i += 1

            return res >= p
        
        nums.sort()
        high = nums[-1] - nums[0]
        low = 0

        while low < high:
            mid = low + (high - low)//2

            if search(mid):
                high  = mid
            else:
                low = mid + 1
        
        return high

