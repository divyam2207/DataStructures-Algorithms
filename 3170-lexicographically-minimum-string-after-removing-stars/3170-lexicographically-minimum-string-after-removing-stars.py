class Solution:
    def clearStars(self, s: str) -> str:

        d1 = defaultdict(list)
        res = [x for x in s]

        for i in range(len(s)): 
            if s[i] != "*":
                d1[s[i]].append(i)
            else:
                for j in range(26):
                    char = chr(ord('a')+j)
                    if d1[char]:
                        res[d1[char][-1]] = "-"
                        d1[char].pop()
                        break
        
        ans = ""

        for each in res:
            if each != "-" and each != "*":
                ans += each
        
        return ans