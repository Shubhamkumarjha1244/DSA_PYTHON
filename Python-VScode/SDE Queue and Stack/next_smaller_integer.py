def next_smaller_element_linear(arr):
    stack=[]
    nsi=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while len(stack) !=0 and stack[-1]>=arr[i]:
            stack.pop()
        if len(stack) !=0:nsi[i]=stack[-1]
        else:nsi[i]=-1
        stack.append(arr[i])
    return nsi

arr=[3,10,4,2,1,2,6,1,7,2,9]
ans=next_smaller_element_linear(arr)
print(ans)

