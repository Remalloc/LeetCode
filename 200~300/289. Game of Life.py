from copy import deepcopy


class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_copy = deepcopy(board)
        rows = len(board_copy)
        cols = len(board_copy[0])

        def in_count(nums):
            live = 0
            for num in nums:
                if num:
                    if board_copy[num[0]][num[1]]:
                        live += 1
            return live

        def out_count(row, col):
            nums = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1), 0, (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            if row == 0:
                nums[0], nums[1], nums[2] = 0, 0, 0
            if row == rows - 1:
                nums[6], nums[7], nums[8] = 0, 0, 0
            if col == 0:
                nums[0], nums[3], nums[6] = 0, 0, 0
            if col == cols - 1:
                nums[2], nums[5], nums[8] = 0, 0, 0
            return in_count(nums)

        for row in range(rows):
            for col in range(cols):
                live = out_count(row, col)
                if board_copy[row][col]:
                    if live < 2 or live > 3:
                        board[row][col] = 0
                elif live == 3:
                    board[row][col] = 1
