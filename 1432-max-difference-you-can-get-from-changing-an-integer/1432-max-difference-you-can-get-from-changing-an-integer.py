class Solution:
    def maxDiff(self, num: int) -> int:
        n1 = str(num)
        n2 = str(num)
        maxi = num

        for i in range(len(n1)):
            if n1[i] == '9':
                continue
            else:
                maxi = max(maxi, int(n1.replace(n1[i], '9')))
                break
        
        
        no = set(n2[0])
        no.add('0')
        changed = False
        mini = num

        for i in range(1,len(n2)):
            if n2[i] not in no:
                mini = int(n2.replace(n2[i], '0'))
                changed = True
                break
        
        mini2 = int(n2.replace(n2[0], '1'))
        mini = min(mini, mini2)

        return maxi - mini