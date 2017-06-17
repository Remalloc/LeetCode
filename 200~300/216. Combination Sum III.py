class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def combination(now_sum, num, level):
            if level > k:
                if now_sum == n:
                    result.append(num[:])
                return
            if not num:
                loop = 1
            else:
                loop = num[-1] + 1
            for i in range(loop, n + 1):
                if i > 9:
                    break
                num.append(i)
                combination(now_sum + i, num, level + 1)
                num.pop()

        combination(0, [], 1)
        return result