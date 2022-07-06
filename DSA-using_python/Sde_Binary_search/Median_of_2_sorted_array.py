def merge(arr1,arr2):
    merge_arr=[0]*(len(arr1)+len(arr2))
    i,j,k=0,0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merge_arr[k]=arr1[i]
            i+=1
            k+=1
        else:
            merge_arr[k]=arr2[j]
            j+=1
            k+=1
    while i<len(arr1) or j<len(arr2):
        if i<len(arr1):
            merge_arr[k]=arr1[i]
            i+=1
            k+=1
        elif j<len(arr2):
            merge_arr[k]=arr2[j]
            j+=1
            k+=1

    print(merge_arr)
    return merge_arr

    

def Median_of_2_sorted_array_basicmethod(arr1,arr2):
    merge_arr=merge(arr1,arr2)
    total_len=len(merge_arr)
    if total_len%2==0:return (merge_arr[total_len//2]+merge_arr[(total_len//2)-1])/2
    if total_len%2!=0:return merge_arr[(total_len//2)]



def Median_of_2_sorted_array_basic_efficient_counter_method(arr1,arr2):
    total_len=(len(arr1)+len(arr2))
    median_at=(total_len)//2
    merge_arr=[0]*(median_at+1)
    i,j,k=0,0,0
    while i<len(arr1) and j<len(arr2) and k<=(median_at):
        if arr1[i]<arr2[j]:
            merge_arr[k]=arr1[i]
            k+=1
            i+=1
        else:
            merge_arr[k]=arr2[j]
            k+=1
            j+=1
    while (i<len(arr1) or j<len(arr2)) and k<=(median_at):
        if i<len(arr1):
            merge_arr[k]=arr1[i]
            k+=1
            i+=1
        if j<len(arr2):
            merge_arr[k]=arr2[j]
            k+=1
            j+=1
    
    print(merge_arr)
    if total_len%2==0:return (merge_arr[-1]+merge_arr[-2])/2
    else:return merge_arr[-1]

def   Median_of_2_sorted_array_binary_search(arr1,arr2,len1,len2):
    if len1>len2:
        return Median_of_2_sorted_array_binary_search(arr2,arr1,len1,len2)  #small wale se start hoga 
    atmid=(len1+len2)//2
    st=0
    en=len1-1
    while en>st:
        cut1=((st+en)//2)
        cut2=atmid-cut1
        
        if cut1==0 :l1=-1000000
        else:l1=arr1[cut1-1]
        if cut2==0 :l1=1000000
        else:l2=arr2[cut2-1]
        if cut1==len1 :l1=1000000
        else:r1=arr1[cut1]
        if cut2==len2 :l1=-1000000
        else:r2=arr2[cut2]

        if l1<r2 and l2<r1:
            if (len1+len2)%2==0:
                max(l1,l2)
            else:
                (max(l1,l2)+min(r1,r2))//2
        elif l1>r2:
            en=cut1-1
        else:st=cut1+1



    




        




        
arr1 = [1,4,7,10,12,13,14,45,67,67,78]
arr2 = [1,2,3,6,15]
len1=len(arr1)
len2=len(arr2)

print(Median_of_2_sorted_array_basicmethod(arr1,arr2))
print("Second method")
print(Median_of_2_sorted_array_basic_efficient_counter_method(arr1,arr2))
print("binary search method")
print(Median_of_2_sorted_array_binary_search(arr1,arr2,len1,len2))