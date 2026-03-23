class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def depth_first_search(row,col,rows,cols,grid,visited):
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ur=row+r
                uc=col+c
                if ur>=0 and ur<rows and uc>=0 and uc<cols and grid[ur][uc]=='1' and visited[ur][uc]==0:
                    visited[ur][uc]=1
                    depth_first_search(ur,uc,rows,cols,grid,visited)
        rows=len(grid)
        cols=len(grid[0])
        visited=[]
        for i in range(rows):
            lst=[0]*cols
            visited.append(lst)
        c=0
        for row in range(0,rows):
            for col in range(0,cols):
                if grid[row][col] == '1' and visited[row][col]==0:
                    visited[row][col]=1
                    depth_first_search(row,col,rows,cols,grid,visited)
                    c+=1
        return c 