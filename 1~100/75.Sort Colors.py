class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = -1
        white = -1
        blue = -1
        for idx in range(len(nums)):
            if nums[idx] == 0:
                blue += 1
                nums[blue] = 2
                white += 1
                nums[white] = 1
                red += 1
                nums[red] = 0
            elif nums[idx] == 1:
                blue += 1
                nums[blue] = 2
                white += 1
                nums[white] = 1
            else:
                blue += 1
                nums[blue] = 2
