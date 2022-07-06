def safe_to_put(row,col,val,solution):
    for i in range(9):
        if solution[i][col] == val :   return False
        if solution[row][i] == val :   return False
        if solution[3*(row//3)+i//3][3*(col//3)+i%3] == val : return False
    return True


def solutionfinder(suduko):
    for i in range(9):
        for j in range(9):
            if suduko[i][j]==0:
                for val in range(1,10):
                    if safe_to_put(i,j,val,suduko) is True:
                        suduko[i][j]=val
                        if solutionfinder(suduko):
                            return True
                        else:
                            suduko[i][j]=0
                return False
    return True



suduko=[
    [0,9,0,0,0,7,4,0,0],
    [1,0,0,0,0,0,8,0,0],
    [0,0,4,0,6,9,0,0,0,],
    [8,0,0,0,4,0,0,1,2],
    [0,0,0,0,0,0,0,0,0],
    [9,4,0,0,5,0,0,0,6],
    [0,0,0,7,8,0,1,0,0],
    [0,0,1,0,0,0,0,0,5],
    [0,0,6,5,0,0,0,8,0],]
suduko1= [[0 for i in range(9)] for i in range(9)]
for ele in suduko:
    print(ele)
print('--------')
print(solutionfinder(suduko))
for ele in suduko:
    print(ele)