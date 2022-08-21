import heapq

li=[3,6,7,8,2,4]

heapq._heapify_max(li)                                       #function 1
print(li)

print(heapq._heappop_max(li))                                #function 2

heapq._heapreplace_max(li,0)                                 #function 3
print(li)


li.append(1)
heapq._siftdown_max(li,0,len(li)-1)                        #function 4
print(li)