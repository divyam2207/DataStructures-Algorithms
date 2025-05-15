class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #start from 0
        def finder(start):
            l = len(words)-1

            for i in range(len(words)):
                if groups[i] == start:
                    l = i
                    break

            res = [words[l]]
            curr = start
            for i in range(l+1, len(words)):
                if groups[i] != curr:
                    res.append(words[i])
                    curr = groups[i]
            
            return res

        r1, r2 = finder(0), finder(1)
        if len(r1) > len(r2):
            return r1
        
        return r2


