class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10
        for i in range(len(digits)):
            count[digits[i]] += 1
        
        res = 0
        
        for one in [0,2,4,6,8]:

            if count[one] > 0:
                count[one] -= 1

                for ten in range(0,10):
                    if count[ten] > 0:
                        count[ten] -= 1

                        for hund in range(1,10):
                            if count[hund] > 0:
                                count[hund] -= 1
                                res += 1
                                count[hund] += 1

                        count[ten] += 1
                count[one] += 1

        return res