def max_val_knapsack(i,weight,value,cap,dp):  
    if i>=len(weight):return 0

    if weight[i]>cap:
        if dp[i+1][cap]==-1:
            dp[i+1][cap]=max_val_knapsack(i+1,weight,value,cap,dp)
        dp[i][cap]=dp[i+1][cap]
        return dp[i][cap]
    else:
        if dp[i+1][cap]==-1:
            dp[i+1][cap]=max_val_knapsack(i+1,weight,value,cap,dp)
        v1=dp[i+1][cap]
        if dp[i+1][cap-weight[i]]==-1:
            dp[i+1][cap-weight[i]]=max_val_knapsack(i+1,weight,value,cap-weight[i],dp)
        v2=value[i]+dp[i+1][cap-weight[i]]
        dp[i][cap]=max(v1,v2)
        return dp[i][cap]



        
    
weight=[12,7,11,8,9]
value=[24,13,23,15,16]
cap =26

dp=[[-1 for j in range(cap+1)] for i in range(len(weight)+1) ]
for i in range(cap+1):dp[-1][i]=0
print(max_val_knapsack(0,weight,value,cap,dp))