class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #backtracking + DFS
        #iterate through every elem in grid, marking if seen
        #if reaches a 1, increment count, dfs search for all connecting 1s

        def dfs(grid, r, c): #check if surrounding elems are == 1, if returns true increment count += 1
            if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] == "0"):
                return False
            grid[r][c] = "0"
            return (dfs(grid, r+1, c) or dfs(grid, r-1, c) or dfs(grid, r, c+1) or dfs(grid, r, c-1))

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    count += 1
        
        return count



            




        