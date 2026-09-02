class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        values=list(d.values())
        for i in range (len(values)):
            for j in range (i+1,len(values)):
                if values[i]==values[j]:
                    return False
        return True                   