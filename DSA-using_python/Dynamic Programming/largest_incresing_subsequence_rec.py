def lis(st,arr,dp):
    max_len=0
    for i in range(len(arr)-1,st-1,-1):
        max_seq=0
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                if dp[j]!=-1:
                    max_seq=max(max_seq,dp[j])
                else:
                    lis(j,arr,dp)
                    dp[i]=1+dp[j]
                    max_seq=max(max_seq,dp[j])
        dp[i]=1+max_seq
        max_len=max(max_len,dp[i])
    print(dp)
    return max_len



arr=[int(ele) for ele in input().split(' ')]
dp=[-1 for i in range(len(arr))]
dp[-1]=1
print(lis(0,arr,dp))