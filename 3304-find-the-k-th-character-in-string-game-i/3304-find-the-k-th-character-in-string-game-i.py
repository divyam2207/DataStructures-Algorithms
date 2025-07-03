class Solution:
    def kthCharacter(self, k: int) -> str:
        s = [97]
        while len(s) <= k +1:
            for i in range(len(s)):
                app = s[i]+1
                if app > 122:
                    app = 96
                s.append(app)
                
        return chr(s[k-1])