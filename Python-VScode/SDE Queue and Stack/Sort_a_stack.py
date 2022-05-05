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

stack=[6,8,2,3,5,7,-1,9876543]
print('unsorted stack---',stack)
sort_a_stack(stack)
print('sorted stack(highest one on top or stack[-1]---',stack)