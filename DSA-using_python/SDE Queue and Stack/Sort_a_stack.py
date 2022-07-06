def arrange_stack(stack,temp):
    if not stack or stack[-1]<temp:
        stack.append(temp)
        return
    top=stack.pop()
    arrange_stack(stack,temp)
    stack.append(top)
    return

def sort_a_stack(stack):
    if not stack: return
    temp=stack.pop()
    sort_a_stack(stack)
    arrange_stack(stack,temp)
    return
stack=[]
for i in range(int(input('Size of stack--'))):
    stack.append(int(input('enter Element--')))

sort_a_stack(stack)
print('sorted stack(highest one on top or stack[-1]---',)
while stack:
    print(stack.pop())