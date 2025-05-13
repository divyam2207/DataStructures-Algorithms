class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        res = 0
        counter = [0]*26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1

        while t>0:
            temp_counter = [0]*26
            for i in range(26):
                if counter[i] > 0:
                    if i<25:
                        temp_counter[i+1] += counter[i]
                    else:
                        temp_counter[0] += counter[25]
                        temp_counter[1] += counter[25]
            counter = temp_counter[:]        
            t -= 1
        
        for each in counter:
            res += (each % MOD)
        return res % MOD
