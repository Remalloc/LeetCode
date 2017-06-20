class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        path = []
        mlen = len(nums)

        def dfs(index):
            if index == mlen:
                return
            for i in range(index, mlen):
                path.append(nums[i])
                result.append(path[:])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
