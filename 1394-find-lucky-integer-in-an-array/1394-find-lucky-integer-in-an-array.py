class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        arr.sort()
        prev = arr[-1]
        freq = 1

        for i in range(len(arr)-2, -1, -1):
            if arr[i] == prev:
                freq += 1
            else:
                if freq == prev:
                    return prev
                else:
                    prev = arr[i]
                    freq = 1
        if freq == prev:
            return prev
        return res