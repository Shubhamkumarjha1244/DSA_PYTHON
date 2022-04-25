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
    [9,5,7,0,1,3,0,8,4],
    [4,8,3,0,5,7,1,0,6],
    [0,1,2,0,4,9,5,3,7],
    [1,7,0,3,0,4,9,0,2],
    [5,0,4,9,7,0,3,6,0],
    [3,0,9,5,0,8,7,0,1],
    [8,4,5,7,9,0,6,1,3],
    [0,9,1,0,3,6,0,7,5],
    [7,0,6,1,8,5,4,0,9],]
suduko1= [[0 for i in range(9)] for i in range(9)]
for ele in suduko:
    print(ele)
print('--------')
print(solutionfinder(suduko))
for ele in suduko:
    print(ele)