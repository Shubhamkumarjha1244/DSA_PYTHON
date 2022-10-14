def max_profit_job_sequencing(n,arr):
    arr.sort(reverse=True,key=lambda a:a[2])
    max_time_limit=max([a[1] for a in arr])
    ans=[-1 for i in range(max_time_limit)]
    for ele in arr:
        for i in range(ele[1]-1,-1,-1):
            if ans[i]==-1:
                ans[i]=ele[2]
                break
    su=0
    co=0
    for ele in ans:
        if ele!=-1:
            su+=ele
            co+=1
    return co,su















n=4
job=[(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
print(max_profit_job_sequencing(n,job))