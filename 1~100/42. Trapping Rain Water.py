class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        total = 0
        left = 0
        right = 0
        idx = 0
        while idx < len(height):
            if not left:
                left = idx
            elif height[left] <= height[idx]:
                result += total
                left = idx
                total = 0
            else:
                total += height[left] - height[idx]
            idx += 1
        if total:
            idx -= 1
            last = idx
            while height[idx] >= height[last]:
                last = idx
                idx -= 1
            while height[left] > height[idx]:
                total -= idx - left
                left += 1
            result += total

        return result
