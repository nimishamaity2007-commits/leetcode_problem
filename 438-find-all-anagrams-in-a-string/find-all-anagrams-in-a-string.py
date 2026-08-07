class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #step 1:to compute the frequencies of string p
        d1={}
        d2={}                  #stay constant int he whole porgram 
        for j in p:                  
            d2[j]=d2.get(j,0)+1
            #step 2: Do a p length sliding window on s 
            #count the frequencies of characters in substring into d1
        k=len(p)  
        left=0
        ans=[]
        for right in range (len(s)):
            d1[s[right]]=d1.get(s[right],0)+1
            if right>=k-1:
                if d1==d2:
                    ans.append(left)
                    #Removing the outgoing element -left
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left+=1
        return ans                

