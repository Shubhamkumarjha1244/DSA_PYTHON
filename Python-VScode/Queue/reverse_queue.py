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
print('------REVERSE------')
q=queue.Queue()
for i in range(5):
    q.put(i)
reverse(q)
while q.qsize()>0:
    print(q.get())