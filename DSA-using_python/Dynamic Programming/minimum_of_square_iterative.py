import math
import sys
def minimum_square(num):
    dp=[sys.maxsize for i in range(num+1)]
    dp[1]=1
    dp[0]=0
    for i in range(2,num+1):
        mini_sq=sys.maxsize
        for j in range(1,int(math.sqrt(num))+1):
            mini_sq=min(mini_sq,dp[i-(j**2)]+1)
        dp[i]=mini_sq
    return dp[num]
            

    

num=int(input('Enter Number'))
print(minimum_square(num))