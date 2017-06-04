class Solution(object):
    def findDuplicates(self, nums):
        mset=set()
        result=[]
        for i in nums:
            if i in mset:
                result.append(i)
            else:
                mset.add(i)
        return result