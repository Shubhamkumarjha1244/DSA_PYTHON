def lis(arr):
    dp=[-1 for i in range(len(arr))]
    dp[-1]=1
    max_sub_seq_len=0
    for i in range(len(arr)-2,-1,-1):
        sub_seq=0
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                sub_seq=max(sub_seq,dp[j])
        dp[i]=1+sub_seq
        max_sub_seq_len=max(max_sub_seq_len,dp[i])
    print(dp)
    return max_sub_seq_len


arr=[int(ele) for ele in input().split(' ')]
print(lis(arr))