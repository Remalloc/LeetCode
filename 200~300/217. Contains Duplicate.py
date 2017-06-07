class Solution(object):
    def containsDuplicate(self, nums):
        mdict={}
        for i in nums:
            if i in mdict:
                return True
            mdict[i]=0
        return False