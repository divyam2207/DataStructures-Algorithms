class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        curr = 0

        while curr < 3:
            for i in range(len(nums)):
                if nums[i] == curr:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            curr += 1
        
        return nums
