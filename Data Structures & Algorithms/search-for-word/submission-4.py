class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, row, col):
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return False
            
            if (row,col) in visited:
                return False

            if i == len(word)-1 and word[i] == board[row][col]:
                return True
            
            visited.add((row, col))

            if board[row][col] == word[i]:
                for r, c in directions:
                    if dfs(i+1, row+r, col+c):
                        return True

            visited.remove((row,col))
            return False
        
        for r in range(rows):
            for c in range(columns):
                if dfs(0, r, c):
                    return True
        
        return False


