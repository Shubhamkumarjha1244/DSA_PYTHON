import heapq
def kth_largest_element(arr,k):
    heapq._heapify_max(arr)
    for i in range(k-1):
        heapq._heappop_max(arr)
    return arr[0]












arr=[int(ele) for ele in input().split()]
k=int(input('Enter kth value'))
print(kth_largest_element(arr,k))
