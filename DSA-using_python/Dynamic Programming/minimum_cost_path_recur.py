import sys


def minimum_cost_path(i,j,matrix):
    if (i>len(matrix)-1) or (j>len(matrix[0])-1):
        return sys.maxsize
    if (i==len(matrix)-1) and (j==len(matrix[0])-1):
        return matrix[i][j]
    col_wise,row_wise,diagonal_wise=sys.maxsize,sys.maxsize,sys.maxsize
    if i+1<len(matrix):
        if dp[i+1][j]!=-1:col_wise=dp[i+1][j]
        else:
            col_wise=minimum_cost_path(i+1,j,matrix)
            dp[i+1][j]=col_wise
    if j+1<len(matrix[0]):
        if dp[i][j+1]!=-1:row_wise=dp[i][j+1]
        else:
            row_wise=minimum_cost_path(i,j+1,matrix)
            dp[i][j+1]=row_wise
    if i+1<len(matrix) and j+1<len(matrix[0]):
        if dp[i+1][j+1]!=-1:diagonal_wise=dp[i+1][j+1]
        else:
            diagonal_wise=minimum_cost_path(i+1,j+1,matrix)
            dp[i+1][j+1]=diagonal_wise
    print(dp)
    return matrix[i][j]+min(col_wise,row_wise,diagonal_wise)










# n=int(input('total row'))
# m=int(input('total column'))
# matrix=[[0 for i in range(n)] for j in range(m)]
matrix=[[9,6,0,12,90,1],[2,7,8,5,78,6],[1,6,0,5,10,-4],[9,6,2,-10,7,4],[10,-2,0,5,5,7]]
dp=[[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
print(minimum_cost_path(0,0,matrix))
