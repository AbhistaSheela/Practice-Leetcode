class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word

        for i in range(self.rows):
            for j in range(self.cols):
                if self.bt(i, j, 0):
                    return True
        return False

    def bt(self, row, col, idx):
        # base case: all characters matched
        if idx == len(self.word):
            return True

        # boundary + mismatch check
        if (
            row < 0 or row >= self.rows or
            col < 0 or col >= self.cols or
            self.board[row][col] != self.word[idx]
        ):
            return False

        temp = self.board[row][col]
        self.board[row][col] = "$"   # mark visited

        found = (
            self.bt(row + 1, col, idx + 1) or
            self.bt(row - 1, col, idx + 1) or
            self.bt(row, col + 1, idx + 1) or
            self.bt(row, col - 1, idx + 1)
        )

        self.board[row][col] = temp  # backtrack
        return found
