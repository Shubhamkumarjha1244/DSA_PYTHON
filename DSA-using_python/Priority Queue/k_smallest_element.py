import heapq



def heapify_up(arr,count):
    i=count
    while i>0:
        parent=(i-1)//2
        if arr[parent]<arr[i]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
        else:break
def heapify_down(arr,k):
    i=0
    while (2*i)+1<k or (2*i)+2<k:
        left=(2*i)+1
        if (2*i)+2>=k:right_val=-(1e12)
        else:right_val=arr[(2*i)+2]
        maxi=max(arr[i],arr[left],right_val)
        if maxi==arr[i]:break
        if maxi==arr[left]:
            arr[i],arr[left]=arr[left],arr[i]
            i=left
        if maxi==right_val:
            arr[i],arr[(2*i)+2]=arr[(2*i)+2],arr[i]
            i=(2*i)+2



def kth_smallest_element(arr,k):
    for i in range(k):
        heapify_up(arr,i)
    for i in range(k,len(arr)):
        if arr[i]<arr[0]:
            arr[i],arr[0]=arr[0],arr[i]
            heapify_down(arr,k)
    return arr[:k]
            
    
    
    


def kth_smallest_element_inbuild_heap(arr,k):
    heapq._heapify_max(arr[:k]) #we didnt define new variable as i want to reduce space and this method is accepted in this class else we can take variable heap
    for i in range(k,len(arr)):
        if arr[i]<arr[0]:
            heapq._heapreplace_max(arr[:k],arr[i])
    return arr[:k]










arr=[int(ele) for ele in input().split(' ')]
k=int(input('Enter k value'))
print(arr)
print(kth_smallest_element(arr,k))
print('Using inbuild heap')
print(kth_smallest_element_inbuild_heap(arr,k))