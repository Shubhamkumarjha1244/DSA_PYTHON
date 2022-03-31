def partition(arr,st,en):
    pivot=arr[st]
    ind=st
    for i in range(st,en+1):  #seach arr range will change
        if arr[i] < pivot:
            ind +=1
    arr[st],arr[ind] =arr[ind],arr[st]  #swapping
    i,j=st,en
    while i > j:   #imp step to swap smaller and greater
        if arr[i] < pivot:
            i +=1
        elif arr[j] >= pivot: 
            j -=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i +=1
            j -=1
    return ind

    
def quick_sort(arr,st,en):
    if st >= en:
        return 
    pivot=partition(arr,st,en)
    quick_sort(arr,st,pivot-1)
    quick_sort(arr,pivot+1,en)
    return arr
    

arr1=[10000,10,3,4,6,11,11,11,11,11]
en=9
print('unsorted array---',arr1)
st=0
quick_sort(arr1,st,en)
print('sorted array-----',arr1)