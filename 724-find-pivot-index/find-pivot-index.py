class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        s=0
        for i in nums:
            s=s+i
            prefix.append(s)
        for i in range(len(nums)):
            leftSum=prefix[i]
            rightSum=prefix[len(nums)]-prefix[i+1]
            if leftSum==rightSum:
                return i
        return -1        
