def safe_to_put(row,col,val,solution):    
    i=row-1
    while i>=0:
        if solution[i][col]==val:
            return False
        i -=1
    i=col-1
    while i>=0:
        if solution[row][i]==val:
            return False
        i -=1
    #for smaller 3*3
    x=3*(col//3)
    y=3*(row//3)
    i=row
    while i>=x:
        j=col
        while j>=y:
            if solution[i][j]==val:
                return False
            j -=1
        i-=1
    return True

def solutionfinder(row,col,suduko,solution):
    if row==9 and col==9:
            for i in range(9):
                print(solution[i])
            return
  
    if row >9 or col > 9:
        return 
    if suduko[row][col] !=0:
        solution[row][col]=suduko[row][col]
        solutionfinder(row+1,col,suduko,solution)
        solutionfinder(row,col+1,suduko,solution)
    else:
        for i in [1,10]:
            solution[row][col]=i
            solutionfinder(row+1,col,suduko,solution)
            solutionfinder(row,col+1,suduko,solution)
            solution[row][col]=0
        return






def printsudukosolution(suduko):
    solution=[[0 for i in range(9)] for j in range(9)]
    solutionfinder(0,0,suduko,solution)
suduko1=[[0 for i in range(9)] for j in range(9)]
suduko=[[9,0,0,0,2,0,7,5,0],[6,0,0,0,5,0,0,4,0],[0,2,0,4,0,0,0,1,0],[2,0,8,0,0,0,0,0,0],[0,7,0,5,0,9,0,6,0],[0,0,0,0,0,0,4,0,1],[0,1,0,0,0,5,0,8,0],[0,9,0,0,7,0,0,0,4],[0,8,2,0,4,0,0,0,6],]

printsudukosolution(suduko)