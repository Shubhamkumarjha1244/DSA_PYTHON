def findcombination(pos,arr,target,ans,ds):
    if pos==len(arr):
        if target==0:
            print(ds)
            ans.append(ds)
        return
    if arr[pos] <= target:
        ds.append(arr[pos])
        findcombination(pos,arr,target-arr[pos],ans,ds)
        ds.pop()
    findcombination(pos+1,arr,target,ans,ds)
def combinationSum(can,target):
    return findcombination(0,can,target,list(),list())
     

can=[2,3,6,7]
target=7
ans=combinationSum(can,target)
print(ans)