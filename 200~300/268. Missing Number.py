class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        return ((n-1)*n)/2 - sum(nums)