import heapq,queue,copy

def buy_the_ticket(arr,pos):
    qu=queue.Queue()
    heap=copy.deepcopy(arr)
    for i in range(len(arr)):qu.put(i)
    heapq._heapify_max(heap)
    time=0
    while True:
        index=qu.get()
        if arr[index]==heap[0]:
            heapq._heappop_max(heap)
            time+=1
            if index==pos:return time
        else:
            qu.put(index)
    


arr=[int(ele) for ele in input().split(' ')]
pos=int(input('element position'))
print(buy_the_ticket(arr,pos))