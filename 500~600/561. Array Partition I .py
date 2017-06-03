# -*- coding: utf-8 -*-
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum=0
        for i in range(len(nums)):
            if (i+1)%2 !=0:
                sum+=nums[i]
        return sum