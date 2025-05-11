class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for each in arr:
            if each%2 != 0:
                count += 1
            else:
                count = 0
            
            if count == 3:
                return True
        
        return False