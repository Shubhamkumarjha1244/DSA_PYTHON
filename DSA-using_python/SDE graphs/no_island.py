class Solution:
    def dfs_helper(self,i,j):
        self.visit[i][j]=True
        move=[(0,1),(1,0),(-1,0),(0,-1)]
        for ele in move:
            x=i+ele[0]
            y=j+ele[1]
            if x<self.len and y<self.bre and x>=0 and y>=0 and self.grid[x][y]=='1' and self.visit[x][y]==False:
                self.dfs_helper(x,y)  
    def numIslands(self, grid):
        self.len=len(grid)
        self.bre=len(grid[0])
        count=0
        self.visit=[[False for i in range(self.bre)] for j in range(self.len)]
        self.grid=grid
        for i in range(self.len):
            for j in range(self.bre):
                if self.grid[i][j]=='1' and self.visit[i][j]==False:
                    count+=1
                    self.dfs_helper(i,j)            
        return count
n=int(input('Enter length'))
m=int(input('Enter Breath'))
grid=[[input('Enter for  row no-'+str(i)+' column no-'+str(j)) for i in range(m)] for j in range(n)]
sol=Solution()
print(sol.numIslands(grid))

