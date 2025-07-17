class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        prev = nums[0]%2
        odd = 1 if prev else 0
        even = 1 if not prev else 0
        alt = 1

        for i in range(1, len(nums)):
            if prev != nums[i]%2:
                alt += 1
                prev = nums[i]%2
            if nums[i]%2 == 0:
                even +=1
            else: 
                odd+=1
        return max(alt, odd, even)