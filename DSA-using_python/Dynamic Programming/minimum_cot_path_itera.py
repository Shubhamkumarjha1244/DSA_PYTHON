from copy import deepcopy
import sys


def minimum_cost_path(matrix):
    dp=deepcopy(matrix)
    dp.append([sys.maxsize for i in range(len(matrix[0]))])
    for col in dp:col.append(sys.maxsize)
    dp[len(matrix)-1][len(matrix[0])-1]=matrix[len(matrix)-1][len(matrix[0])-1]
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,-1,-1):
            if i==len(matrix)-1 and j==len(matrix[0])-1:continue
            dp[i][j]=min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+matrix[i][j]
    return dp[0][0]

# n=int(input('total row'))
# m=int(input('total column'))
# matrix=[[0 for i in range(n)] for j in range(m)]
matrix=[[9,6,0,12,90,1],[2,7,8,5,78,6],[1,6,0,5,10,-4],[9,6,2,-10,7,4],[10,-2,0,5,5,7]]
matrix1=[[3,4,1,2],[2,1,8,9],[4,7,8,1]]
matrix2=[[10,6,9,0],[-23,8,9,90],[-200,0,89,200]]
print(minimum_cost_path(matrix))
