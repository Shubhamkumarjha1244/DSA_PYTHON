def maximum_sum_increase(arr):
    dp=[-1 for i in range(len(arr)+1)]
    dp[-1]=0
    max_sum=0
    for i in range(len(arr)-1,-1,-1):
        max_till=0
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                max_till=max(max_till,dp[j])        
        dp[i]=arr[i]+max_till
        max_sum=max(max_sum,dp[i])
    print(dp)
    return max_sum


arr=[int(ele) for ele in input('Enter Number in array').split(' ')]
print(maximum_sum_increase(arr))