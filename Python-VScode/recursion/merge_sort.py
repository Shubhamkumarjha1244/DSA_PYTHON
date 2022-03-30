def merge(arr1,arr2,arr):
    i,j,k=0,0,0

    while i < len(arr1) and j < len(arr2) :
        if arr2[j] > arr1[i]:
            arr[k]=arr1[i]
            k +=1
            i +=1 
        else:
            arr[k] =arr2[j]
            k += 1
            j += 1
    while i < len(arr1):
            arr[k]=arr1[i]
            k +=1
            i +=1
    while j <len(arr2):
            arr[k] =arr2[j]
            k += 1
            j += 1
    
    return arr






def merge_sort(arr):
    if len(arr)==1 or len(arr)==0:
        return
    mid=len(arr)//2
    a1=arr[mid:]
    a2=arr[:mid]
    merge_sort(a1)            #last case me problem kar dega dyan rakho
    merge_sort(a2)
    merge(a1,a2,arr)
    return arr

    

arr1=[1000000,4,2,7,9,8,10,11,46] 
print('unsorted array---',arr1)


merge_sort(arr1)
print('sorted array-----',arr1)

