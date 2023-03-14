class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(pos: tuple):
            x, y = pos

            if not (x < len(grid) and x >=0) or not (y < len(grid[0]) and y >=0):
                return
            
            if grid[x][y] == '0':
                return

            grid[x][y] = '0'

            next_step = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            while next_step:
                dfs(next_step.pop())

        answer = 0

        for i in range(len(grid)): # m
            for j in range(len(grid[0])): # n
                if grid[i][j] == '1':
                    dfs((i, j))
                    answer += 1
        
        return answer