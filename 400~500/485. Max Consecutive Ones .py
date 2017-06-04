class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxnum = 0
        mlen = len(nums)
        for i in range(mlen):
            if nums[i] == 1:
                cnt += 1
            else:
                maxnum = cnt if cnt > maxnum else maxnum
                cnt=0
        maxnum = cnt if cnt > maxnum else maxnum
        return maxnum