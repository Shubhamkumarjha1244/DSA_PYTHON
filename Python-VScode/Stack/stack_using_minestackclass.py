
from stack_using_LL_class import stack

shubham=stack()
for i in range(1,6):
    shubham.push(i)

print('TOP---',shubham.top())
print('LENGTH--',shubham.length())
while not shubham.isEmpty():
    print(shubham.pop())
print('POPING DONE')
print('IS EMPTY---',shubham.isEmpty())


