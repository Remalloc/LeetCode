class Solution(object):
    def twoSum(self, numbers, target):
        numlen = len(numbers)
        last=None
        for i in range(numlen):
            if numbers[i]==last and numbers[i]+last!=target:
                continue
            last=numbers[i]
            subnum=target-last
            for j in range(i+1,numlen):
                if numbers==subnum:
                    return [i+1,j+1]
