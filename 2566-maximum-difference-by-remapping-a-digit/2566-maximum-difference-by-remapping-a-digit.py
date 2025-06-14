class Solution:
    def minMaxDifference(self, num: int) -> int:
        n1,n2 = str(num), str(num)
        maxi, mini = num, num

        for i in range(len(n1)):
            if n1[i] != '9':
                maxi = int(str(n1.replace(n1[i], '9')))
                break

        for i in range(len(n2)):
            if n2[i] != '0':
                mini = int(str(n2.replace(n2[i], '0')))
                break
        

        return maxi - mini