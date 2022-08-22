
import collections
from queue import PriorityQueue  
def KMostFrequent(arr,k):
    co=collections.Counter(arr)
    print(co)
    pq=PriorityQueue()
    for ele in co.keys():
        pq.put((-(co[ele]),ele)) #to use it as priority queue we can pass tuple as (priority,value) v.v.v.i
    ans=[]
    for i in range(k):
        temp=pq.get()
        ans.append(temp[1])
    return ans
    


arr=[int(ele) for ele in input().split(' ')]
k=int(input('k value'))
print(KMostFrequent(arr,k))
