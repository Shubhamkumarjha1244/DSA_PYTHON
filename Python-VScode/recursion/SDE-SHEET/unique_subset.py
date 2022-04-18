def unique(pos,arr,ans,out):
    print(ans)
    for i in range(pos,len(arr)) :
        if i !=pos and arr[i]==arr[i-1]:
            continue
        ans.append(arr[i])
        unique(i+1,arr,ans,out)
        ans.pop()

def print_unique(arr):
    output=[]
    arr.sort()
    unique(0,arr,list(),output)
    print(output)
    return
arr=[1,2,2]
print_unique(arr)
