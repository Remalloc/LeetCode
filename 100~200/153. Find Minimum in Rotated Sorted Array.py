class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1

        while True:
            mid = (begin + end) // 2
            if nums[begin] < nums[mid]:
                if nums[begin] < nums[end]:
                    return nums[begin]
                begin = mid + 1
            elif nums[begin] > nums[mid]:
                end = mid
            else:
                return nums[begin] if nums[begin] < nums[end] else nums[end]
        return nums[mid]
