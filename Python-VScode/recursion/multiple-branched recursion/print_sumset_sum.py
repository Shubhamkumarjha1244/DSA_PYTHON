def inputarr(n):
    a=[int(ele) for ele in input().split(' ')]
    if len(a) != n:
        print('SIZE MISMATCH')
        return
    return a
    


def print_sum_subset(num_arr,ans,n):
    if len(num_arr)==0:
        sum=0
        for i in ans:
            sum=sum+i
        if sum==n:
            print(ans)
            return
        else:
            return
    print_sum_subset(num_arr[1:],ans,n)
    incl=ans+[num_arr[0]]
    print_sum_subset(num_arr[1:],incl,n)
n=input('Enter length of array')
num_arr=inputarr(n)
# num_arr=[5,12,3,17,1,18,15,3,17]
if num_arr:
    print_sum_subset(num_arr,[],6)