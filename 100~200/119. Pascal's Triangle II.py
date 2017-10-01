class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri = [1]
        for i in range(1, rowIndex + 1):
            tri.append(1)
            for j in range(i + 1):
                now = tri[j]
                if j != 0 and j != i:
                    tri[j] += last
                last = now
        return tri
