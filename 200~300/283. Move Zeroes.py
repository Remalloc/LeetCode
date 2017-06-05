class Solution(object):
    def moveZeroes(self, nums):
        cnt=0
        i=0
        mlen=len(nums)
        while i<mlen:
            if nums[i]==0:
                del nums[i]
                cnt+=1
                i-=1
                mlen-=1
            i+=1
        for i in range(cnt):
            nums.append(0)