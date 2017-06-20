class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mlen = len(nums)
        i = 0
        result = []
        while i < 1 << mlen:
            j = 0
            temp_list = []
            while j < mlen:
                if i & 1 << j:
                    temp_list.append(nums[j])
                j += 1
            result.append(temp_list)
            i += 1
        return result
