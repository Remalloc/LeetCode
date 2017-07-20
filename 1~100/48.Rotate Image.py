class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        mlen = len(matrix)
        row = 0
        result = []
        while row < mlen:
            column = mlen - 1
            temp = []
            while column >= 0:
                temp.append(matrix[column][row])
                column -= 1
            result.append(temp)
            row += 1
        matrix[:] = result
        