from typing_extensions import Self
import Queue_using_array

q=Queue_using_array.queue()


arr=[1,2,3]

for i in range(len(arr)):
    q.enqueue(arr[i])

n=int(input("Enter A number of cycle"))
n=n%(len(arr))
for i in range(n):
    q.enqueue(q.dequeue())

while q.isEmpty()==False:
    print(q.dequeue(),end=",")

