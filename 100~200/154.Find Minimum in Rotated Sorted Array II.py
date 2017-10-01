class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if len(nums) <= 2:
            return min(nums[left], nums[right])

        def fun(left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid - 1] <= nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                if nums[mid - 1] > nums[mid] <= nums[mid + 1]:
                    return nums[mid]
                reply = fun(mid + 1, right)
                if reply is not None:
                    return reply
                reply = fun(left, mid - 1)
                if reply is not None:
                    return reply
                else:
                    return

        reply = fun(left, right)
        return reply if reply is not None else min(nums[left], nums[right])
