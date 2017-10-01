class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if lens == 1:
            return 0
        if lens == 2:
            return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]:
            return 0
        if nums[lens - 1] > nums[lens - 2]:
            return lens - 1
        for mid in range(1, lens - 1):
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
