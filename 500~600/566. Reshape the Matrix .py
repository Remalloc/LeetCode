class Solution(object):
    def matrixReshape(self, nums, r, c):
        temp = []
        for i in nums:
            for j in i:
                temp.append(j)
        if len(temp)!=r*c:
            return nums
        result = []
        cnt=0
        for row in range(r):
            result.append(temp[cnt:cnt+c])
            cnt+=c
        return result