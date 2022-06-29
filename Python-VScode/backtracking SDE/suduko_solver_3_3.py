def safe_to_put(row,col,val,solution):
    for i in range(3):
        if solution[i][col] == val :   return False
        if solution[row][i] == val :   return False
    return True

def solutionfinder(suduko):
    for i in range(3):
        for j in range(3):
            if suduko[i][j]==0:
                for val in range(1,4):
                    if safe_to_put(i,j,val,suduko) is True:
                        suduko[i][j]=val
                        if solutionfinder(suduko):
                            return True
                        else:
                            suduko[i][j]=0
                return False
    return True





suduko2= [[0 for i in range(3)] for i in range(3)]
suduko1=[[0,1,0],[0,0,2],[0,0,2]]
for ele in suduko2:
    print(ele)
print('--------')
print(solutionfinder(suduko2))
for ele in suduko2:
    print(ele)