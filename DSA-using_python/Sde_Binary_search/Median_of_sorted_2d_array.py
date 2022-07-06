
def smaller(arr,num):
    st=0
    en=len(arr)-1
    while en>st:
        mid=(st+en)//2
        if arr[mid]<=num:
            st=mid+1
        if arr[mid]>num:
            en=mid-1 #vvi -1 should be taken care
    print('start',arr,st)
    return st
        
def median_sorted_2d_array(arr):
    st=0
    en=1e9
    while en>st:
        mid=int((st+en)//2)
        smaller_than_median=int((len(arr)**2)//2)
        smaller_num=0
        for ele in arr:
            smaller_num+=smaller(ele,mid)
        if smaller_num<smaller_than_median:
            st=mid
        if smaller_num>=smaller_than_median:
            en=mid
        print('next','mid--',mid,"start--",st,'end--',en)
    return st
arr=[[1,3,5],[2,6,9],[3,6,9]]
print(median_sorted_2d_array(arr))