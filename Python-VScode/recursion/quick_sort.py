def swap(arr,p1,p2):
    temp=arr[p1]
    arr[p1]=arr[p2]
    arr[p2]=temp
    return arr




def quick_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    pi=arr[len(arr//2)]
    i=0
    j=len(arr)-1
    while j > i :
        while arr[i]<pi:
            i +=1
        while arr[j]>pi:
            j -=1
        swap(arr,i,j)
    quick_sort(arr[:mid])
    quick_sort(arr[mid:])
    return arr
        
arr=[100000,1,2,7,6,5,8,9,10]
print(quick_sort(arr))
  


