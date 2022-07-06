from Stack_using_single_Queue import stack_using_single_queue

shubham=stack_using_single_queue()
for i in range(1,6):
    shubham.push(i)

print('TOP---',shubham.top())
print('LENGTH--',shubham.size())
while not shubham.isEmpty():
    print(shubham.pop())
print('POPING DONE')
print('IS EMPTY---',shubham.isEmpty())