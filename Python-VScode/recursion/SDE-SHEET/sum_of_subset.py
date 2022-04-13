def sum_subset(arr,ans):
    if len(arr)==0:
        print(ans,end=' ')
        return
    ele=arr[0]
    sum_subset(arr[1:],ans)
    new_ans=ans+ele
    sum_subset(arr[1:],new_ans)



arr=[5,2,1]
sum_subset(arr,0)