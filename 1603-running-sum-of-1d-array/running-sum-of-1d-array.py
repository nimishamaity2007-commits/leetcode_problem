class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num=[]
        s=0
        for i in nums:
            s=s+i
            num.append(s)
        return num  

        