class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        d2={}                  #stay constant int he whole porgram 
        for j in s1:                  
            d2[j]=d2.get(j,0)+1
        k=len(s1)  
        left=0
        ans=[]
        for right in range (len(s2)): 
            d1[s2[right]]=d1.get(s2[right],0)+1
            if right>=k-1:
                if d1==d2:
                    return True#if anagrams adding start index to ans 
                    #Removing the outgoing element -left
                d1[s2[left]]-=1
                if d1[s2[left]]==0:
                    d1.pop(s2[left])
                left+=1
        return False       