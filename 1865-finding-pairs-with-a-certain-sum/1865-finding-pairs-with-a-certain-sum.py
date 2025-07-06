class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.d1 = defaultdict(int)

        for i in range(len(nums1)):
            self.d1[i] = nums1[i]
        
        self.d2 = Counter(nums2)
        self.d3 = {k:v for k,v in enumerate(nums2)}
        

    def add(self, index: int, val: int) -> None:
        num_to_change = self.d3[index]
        self.d2[num_to_change + val] += 1
        self.d2[num_to_change] -= 1
        self.d3[index] = num_to_change + val

    def count(self, tot: int) -> int:

        res = 0
        for i, v in self.d1.items():
            res += self.d2[tot - v]
        
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)