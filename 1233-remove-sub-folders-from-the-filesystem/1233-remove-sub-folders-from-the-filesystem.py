class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x: len(x))
        root = set()
        for i in range(len(folder)):
            if folder[i].count("/") == 1:
                if folder[i] not in root:
                    root.add(folder[i])
            else:
                temp = ""
                flag = True
                for each in folder[i][1:].split("/"):
                    if (temp+"/"+each) in root: 
                        flag = False  
                        break
                    temp += "/"+each
                if flag:
                    root.add(temp)
        return [x for x in root]
                   
