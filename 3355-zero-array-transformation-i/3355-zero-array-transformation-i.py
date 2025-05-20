class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta = [0] * (len(nums)+1)

        for l,r in queries:
            delta[l] += 1
            delta[r+1] -= 1
        

        for i in range(1,len(nums)+1):
            delta[i] += delta[i-1]
        
        for i in range(len(nums)):
            if nums[i] > delta[i]:
                return False
        
        return True