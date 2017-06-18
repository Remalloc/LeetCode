class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m={}
        cnt=0
        msum=0
        for i in nums:
            m[msum]=m.get(msum,0)+1
            msum+=i
            if msum-k in m:
                cnt+=m[msum-k]
        return cnt