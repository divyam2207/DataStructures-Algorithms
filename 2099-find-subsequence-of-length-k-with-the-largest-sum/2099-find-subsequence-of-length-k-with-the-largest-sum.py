class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [[idx, num] for idx, num in enumerate(nums)]

        arr = sorted(arr, key=lambda x: x[1], reverse = True)

        ladder = arr[:k]
        ladder = sorted(ladder, key = lambda x: x[0])

        return [x for y,x in ladder]
