class Solution(object):
    def arrayNesting(self, nums):
        mset = set()
        maxset=0
        for i in nums:
            value=i
            cnt=0
            while value not in mset:
                mset.add(value)
                value=nums[value]
                cnt+=1
            if maxset<cnt:
                maxset=cnt
        return maxset