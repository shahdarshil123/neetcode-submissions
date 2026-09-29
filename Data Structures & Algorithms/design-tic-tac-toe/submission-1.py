class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for i in range(n)]
        self.n = n
        self.directions = [[(0,1), (0,-1)], [(1,0),(-1,0)], [(-1,-1), (1,1)], [(-1,1),(1,-1)]]

    def move(self, row: int, col: int, player: int) -> int:
        # place the move
        self.board[row][col] = player

        # check the count
        max_count = 0
        for i in range(len(self.directions)):
            count = 1
            for j in range(len(self.directions[i])):
                dr, dc = self.directions[i][j]
                r, c = row, col
                while 0 <= r + dr < self.n and 0 <= c + dc < self.n and self.board[r+dr][c+dc] == player: 
                    count += 1
                    r = r + dr
                    c = c + dc
            max_count = max(max_count, count)
        
            if max_count == self.n:
                return player
        
        return 0
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)