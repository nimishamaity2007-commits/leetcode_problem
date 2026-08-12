class NumArray:

    def __init__(self, nums: List[int]):
        self.num=[]
        s=0
        for i in nums:
            s=s+i
            self.num.append(s)
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return (self.num[right])
        else:
            su=self.num[right]-self.num[left-1]
            return su             #return (self.num[r+1]-self.num[l])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)