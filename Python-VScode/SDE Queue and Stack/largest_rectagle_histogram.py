def largest_rectangle_histogram_using_2_pass(arr):
    stack=[]
    shl=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if len(stack)!=0:shl[i]=stack[-1]
        else:shl[i]=len(arr)
        stack.append(i)       
    stack=[]
    shr=[0]*len(arr)
    for i in range(0,len(arr),1):
        while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if len(stack)!=0:shr[i]=stack[-1]
        else:shr[i]=-1
        stack.append(i)
    arealist=[0]*len(arr)
    # print("smallest element end side se--",shl)
    # print("smallest element start side se--",shr)
    for i in range(len(arr)):
        arealist[i]=arr[i]*(shl[i]-shr[i]-1)
    print(arealist)
    return max(arealist)

# arr=[2,1,5,6,2,3,2,1,5,6,2,3,]
# print(arr)
# print(largest_rectangle_histogram_using_2_pass(arr))


def largest_rectangle_histogram_using_1_pass(arr):
        
    stack=[]
    area=[0]*len(arr)
    arr.append(0)
    for i in range(0,len(arr),1):
        while len(stack)!=0 and arr[i]<=arr[stack[-1]]:
                rightlower=i
                ind=stack.pop()
                height=arr[ind]
                if len(stack)!=0:leftlower=stack[-1]
                else:leftlower=-1
                area[ind]=(rightlower-leftlower-1)*height
        stack.append(i)
    print(area)
    return max(area)
#SDE sheet
def largest_rectangle_youtube(arr):
    stack=[]
    n=len(arr)
    area=[0]*n
    for i in range(n+1):
        while (len(stack)!=0) and ((i==n) or (arr[stack[-1]] >= arr[i])):
                ind=stack[-1]
                height=arr[ind]
                stack.pop
                if len(stack)==0:width=i
                else:width=i-stack[-1]-1
                area[ind]=width*height   
        stack.append(i)
   
    return area


arr=[2,1,5,6,2,3]
print(arr)
print(largest_rectangle_histogram_using_2_pass(arr))
print(largest_rectangle_histogram_using_1_pass(arr))
print(largest_rectangle_youtube(arr))

#teacher





