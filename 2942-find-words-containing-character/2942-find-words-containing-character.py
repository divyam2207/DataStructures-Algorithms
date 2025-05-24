class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        for i in range(len(words)):
            if x in words[i]:
                words[i] = i
            else:
                words[i] = -1
        return [x for x in words if x>-1]