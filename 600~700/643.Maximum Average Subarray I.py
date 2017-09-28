class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tol = 0
        for i in range(k):
            tol += nums[i]
        re = tol

        for i in range(k, len(nums)):
            tol += nums[i] - nums[i - k]
            re = max(re, tol)

        return re/k
