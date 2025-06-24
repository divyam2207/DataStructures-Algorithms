class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        idx = [x for x in range(len(nums)) if nums[x] == key]

        for each in idx:
            for i in range(max(0,each-k), min(len(nums), each+k+1)):
                res.add(i)
            

        return sorted([x for x in res])