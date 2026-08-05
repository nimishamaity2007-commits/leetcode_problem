class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #mx=-10000000
        #for i in range (0,len(nums)):
           # for j in range(i,len(nums)):
               # s=0
              #  for num in range(i,j+1):
                 #   s+=nums[num]
              #  if j-i ==k-1:
                   # avg=s/k
                   # mx=max(mx,avg)
        #return mx 
        mx=-10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right >=k-1:
                avg=currentsum/k
                mx=max(avg,mx)
                currentsum-=nums[left]
                left+=1
        return mx        
