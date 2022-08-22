import heapq
def mergeKSortedArrays(kArrays):
    arr=[]
    for array in kArrays:
        for ele in array:
            heapq.heappush(arr,ele)
    ans=[]
    while len(arr)!=0:
       ans.append(heapq.heappop(arr))
    return ans


length_of_collection=int(input('Number of arr'))
collection_sorted_arr=[]
for i in range(length_of_collection):
    collection_sorted_arr.append([int(ele) for ele in input().split(' ')])
print(mergeKSortedArrays(collection_sorted_arr))
