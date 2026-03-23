from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        queue=deque()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh=1
        if not queue:
            if fresh==1:
                return -1
            else:
                return 0
        time=0
        while queue:
            for i in range(len(queue)):
                curr_i,curr_j=queue.popleft()
                for i_off, j_off in directions:
                    new_i,new_j=curr_i+i_off , curr_j+j_off
                    if new_i < 0 or new_j<0 or new_i>=rows or new_j>=cols:
                        continue
                    if grid[new_i][new_j]!=1:
                        continue
                    grid[new_i][new_j]=2
                    queue.append((new_i,new_j))
            time+=1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return time-1