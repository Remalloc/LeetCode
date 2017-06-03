class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict.keys():
                return (dict[target-x], i)
            dict[x] = i