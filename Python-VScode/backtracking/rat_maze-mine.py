
def print_possible_path(maze):
    n=len(maze)
    solution=[[0 for i in range(n) ] for i in range(n)]
    path_finder(0,0,n,maze,solution)


def path_finder(x,y,n,maze,solution):

    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    if x<0 or y<0 or x>n-1 or y>n-1 or maze[x][y]==0 or solution[x][y]==1:
        return
    solution[x][y]=1
    path_finder(x+1,y,n,maze,solution)
    path_finder(x,y+1,n,maze,solution)
    path_finder(x-1,y,n,maze,solution)
    path_finder(x,y-1,n,maze,solution)
    solution[x][y]=0
    return



n=int(input('no of column in array'))
maze=[]
for i in range(n):
    row=[int(ele) for ele in input().split()]
    maze.append(row)
print(maze)
print_possible_path(maze)