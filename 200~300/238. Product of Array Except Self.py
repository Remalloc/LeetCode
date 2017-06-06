class Solution(object):
    def productExceptSelf(self, nums):
        pronum=1
        cntzero=0
        for i in nums:
            if i!=0:
                pronum*=i
            else:
                cntzero+=1
        result=[]
        for i in nums:
            if i!=0:
                if cntzero:
                    result.append(0)
                else:
                    result.append(pronum/i)
            else:
                if cntzero>1:
                    result.append(0)
                else:
                    result.append(pronum)
        return result
