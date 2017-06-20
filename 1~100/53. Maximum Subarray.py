class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        result = max_sum
        for i in range(1, len(nums)):
            if max_sum + nums[i] < nums[i]:
                max_sum = nums[i]
            else:
                max_sum += nums[i]
            if result < max_sum:
                result = max_sum
        return result
