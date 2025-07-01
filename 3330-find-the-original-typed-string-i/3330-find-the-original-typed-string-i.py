class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        prev = word[0]

        for i in range(1, len(word)):
            if prev == word[i]:
                res += 1
            prev = word[i]

        return res