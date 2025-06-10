class Solution:
    def maxDifference(self, s: str) -> int:
        s = [ch for ch in s]
        s.sort()
        s.append("*")

        prev = s[0]
        count = 1
        odd, min_even = 0,0

        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                if count % 2 == 0:
                    if min_even == 0:
                        min_even = count
                    else:
                        min_even = min(min_even, count)
                else:
                    odd = max(odd, count)
                count = 1
                prev = s[i]
        
        return odd - min_even
        

