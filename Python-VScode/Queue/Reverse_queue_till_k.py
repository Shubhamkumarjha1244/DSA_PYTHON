import queue
def reverse(q:queue.Queue):
    if q.qsize()==0:
        return
    temp=q.get()
    reverse(q)
    q.put(temp)
    return q
q=queue.Queue()
for i in range(5):
    q.put(i)
while q.qsize()>0:
    print(q.get())
q=queue.Queue()
for i in range(5):
    q.put(i)
print('------REVERSE------')
reverse(q)
stack=[]
k=q.qsize()-int(input("Enter k value"))
for i in range(k):
    stack.append(q.get())
for i in range(k):
    q.put(stack.pop())
while q.qsize()>0:
    print(q.get())