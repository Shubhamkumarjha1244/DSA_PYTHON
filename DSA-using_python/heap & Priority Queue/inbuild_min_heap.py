import heapq

li=[9,6,8,4,7,1]

heapq.heapify(li)                                                 #fuction 1

print(heapq.heappop(li))                                          #fuction 2

heapq.heappush(li,11)                                             #fuction 3

heapq.heapreplace(li,111)                                         #fuction 4

print(li)