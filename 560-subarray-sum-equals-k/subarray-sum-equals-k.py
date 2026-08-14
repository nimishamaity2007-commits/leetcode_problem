class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum+ hash map slution
        csum=0 #this is our prefix sum
        subcnt=0 #how many sub  array have we seen with sum k
        seen={0:1} #hash map to store prefix sum found so far
        for i in nums:
            #compute prefix sum
            csum+=i
            #required prefix sum(prefix(l-1),history)
            req=csum-k
            #check if req is seen prefix so far
            if req in seen :
                subcnt+=seen[req]
            seen[csum]=seen.get(csum,0)+1 #add the number of times we seen that prefix 
            #push the current prefix in hashmap
        return subcnt                      

