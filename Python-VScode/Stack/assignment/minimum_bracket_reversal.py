def minimum_reverse(stri):
    stack=[]
    for ele in stri:
        if ele=='(':
            stack.append(ele)
        elif ele==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(ele)
    count=0
    for i in range(len(stack)//2):
        brac1=stack.pop()
        brac2=stack.pop()
        if brac1==brac2:
            count +=1
        elif brac1!=brac2:
            count +=2

    if len(stack) !=0:
        return -1
    else:
        return count

stri=')'
print(minimum_reverse(stri))
        

