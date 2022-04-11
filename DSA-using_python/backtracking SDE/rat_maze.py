
def pathfinder(x,y,maze,n,solution):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        for i in range(n):
                print(solution[i],end='\n')
        print()
        return
    if x<0 or y<0 or x>=n or y>=n or maze[x][y] == 0 or solution[x][y] ==1 :
        return
    solution[x][y]=1
    pathfinder(x+1,y,maze,n,solution)
    pathfinder(x,y+1,maze,n,solution)
    pathfinder(x-1,y,maze,n,solution)
    pathfinder(x,y-1,maze,n,solution)
    solution[x][y]=0
    return



def printpath(maze):
    n=len(maze)
    solution=[[0 for i in range(n)] for j in range(n) ]
    pathfinder(0,0,maze,n,solution)
    


    


# n=int(input("Enter column of array--"))
# maze=[]
# for i in range(n):
#     row=[int(ele) for ele in input().split()]
#     maze.append(row)

printpath([[1,1,1],[1,1,1],[1,1,1]])