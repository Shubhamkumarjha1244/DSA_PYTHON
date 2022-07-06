def maximum_sliding_window(list,k):
    maximum=[]
    for i in range(0,len(list)-k+1):
       small_list=list[i:i+k]
       maximum.append(max(small_list))
    return maximum


# arr=[4,0,-1,3,5,3,6,8]
# k=3
# print(maximum_sliding_window(arr,k))



import collections

def maximum_in_sliding_window(arr,k):
    de=collections.deque() #dobly queue
    max_list=[]
    for i in range(len(arr)):
        if len(de)!=0 and de[-1] == i-k:
            de.pop()
        while len(de)!=0 and arr[de[-1]]<=arr[i]:
            de.popleft()
        de.append(i)
        if i>=k-1:
            max_list.append(arr[de[0]])
        print(de)
    return max_list

arr=[25,1,1,1,1,1]
k=2
print(maximum_sliding_window(arr,k))
print(maximum_in_sliding_window(arr,k))