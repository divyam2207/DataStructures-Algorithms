class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        same = 0
        hashmap = defaultdict(int)
        res = 0

        for each in words:
            if each == each[::-1]:
                same += 1

            if hashmap[each] <= 0:
                hashmap[each[::-1]] += 1
            else:
                if each == each[::-1]:
                    same -= 2
                res += 4
                hashmap[each] -= 1

        return res + 2 if same>0 else res        