
def knapsack_irr(weight,value,cap):
    dp=[[-1 for j in range(cap+1)] for i in range(len(weight)+1) ]
    for i in range(cap+1):dp[-1][i]=0
    for i in range(len(weight)-1,-1,-1):
        for j in range(0,cap+1):
            if weight[i]>j:
                dp[i][j]=dp[i+1][j]
            else:
                w1=dp[i+1][j]
                w2=value[i]+dp[i+1][j-weight[i]]
                dp[i][j]=max(w1,w2)
    return dp[0][cap]
        



weight=[12,7,11,8,9]
value=[24,13,23,15,16]
cap=26
print(knapsack_irr(weight,value,cap))