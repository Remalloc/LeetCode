class Solution(object):
    def findDisappearedNumbers(self, nums):
        res=[]
        for value in nums:
            index=abs(value)-1
            if nums[index]>0:
                nums[index]=-nums[index]
        for index,value in enumerate(nums):
            if value>0:
                res.append(index+1)
        return res