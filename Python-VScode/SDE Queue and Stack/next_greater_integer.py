# # def greater_integer(arr):
# #     stack=[]
# #     ngi=[0]*len(arr)
# #     for i in range(2*len(arr)-1,-1,-1):
# #         while len(stack) != 0 and stack[-1] <= arr[i%len(arr)]:
# #             stack.pop()
# #         if i < len(arr):
# #             if len(stack) !=0 : 
# #                 ngi[i]=stack[-1]
# #             else:ngi[i]=-1
# #         stack.append(arr[i % len(arr)])
# #     print(ngi)

# # arr=[1,5,7,8,9]
# # greater_integer(arr)


# def greater_integer(arr):
#     stack=[]
#     ngi=[0]*len(arr)
#     for i in range(len(arr)-1,-1,-1):
#         while len(stack) != 0 and stack[-1] <= arr[i]:
#             stack.pop()
#         if len(stack) !=0 : 
#             ngi[i]=stack[-1]
#         else:ngi[i]=-1
#         stack.append(arr[i])
#     print(ngi)

# arr=[1,5,2,10,9,1]
# greater_integer(arr)

def next_greater_integer_linear(arr):
    stack=[]
    ngi=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while len(stack) !=0 and stack[-1] <=arr[i] :
            stack.pop()
        if len(stack) !=0 : ngi[i]=stack[-1]
        else: ngi[i]=-1
        stack.append(arr[i])
    return ngi

def next_greater_integer_circular(arr):
    stack=[]
    ngi=[0]*len(arr)
    for i in range(2*len(arr)-1,-1,-1):
        while len(stack) !=0 and stack[-1]<=arr[i%len(arr)]:
            stack.pop()
        if i <len(arr):
            if len(stack)!=0:ngi[i%len(arr)]=stack[-1]
            else: ngi[i%len(arr)]=-1
        stack.append(arr[i%len(arr)])
    return ngi

arr=[3,10,4,2,1,2,6,1,7,2,9] 
print(next_greater_integer_linear(arr))
print(next_greater_integer_circular(arr))   


