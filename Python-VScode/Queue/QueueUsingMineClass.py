from Queue_using_LL import queue

shubham=queue()
print('Queue is Empty',shubham.isEmpty())

print(shubham.enqueue(1))
print(shubham.enqueue(2))
print('Front of queue',shubham.front())
print(shubham.enqueue(3))
print(shubham.enqueue(4))
print('Front of queue',shubham.front())
print(shubham.enqueue(5))

print('length of Queue',shubham.size())
print('Queue is Empty',shubham.isEmpty())
print('Front of queue',shubham.front())
print(shubham.dequeue())
print(shubham.dequeue())
print(shubham.dequeue())
print('Front of queue',shubham.front())
print(shubham.dequeue())
print(shubham.dequeue())
print(shubham.dequeue())

print('length of Queue',shubham.size())
print('Queue is Empty',shubham.isEmpty())
print('Front of queue',shubham.front())
print(shubham.dequeue())
