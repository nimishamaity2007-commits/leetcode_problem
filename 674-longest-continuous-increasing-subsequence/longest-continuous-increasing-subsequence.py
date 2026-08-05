class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count =1
        mx=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                mx=max(mx,count)
                count=1
        return max(mx,count)          