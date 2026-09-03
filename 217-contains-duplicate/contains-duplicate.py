class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n1=len(set(nums))
        n2=len(nums)
        return n1!=n2