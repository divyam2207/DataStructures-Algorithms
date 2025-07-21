class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        res = ""
        res += s[0]
        for i in range(1, len(s)-1):
            if s[i] == s[i-1] and s[i] == s[i+1]:
                continue
            else:
                res+=s[i]

        if len(res) >= 2 and s[-1] == res[-1] and s[-1] == res[-2]:
            pass
        else:
            res += s[-1]
        return res
        