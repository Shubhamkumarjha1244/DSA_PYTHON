# #my_way


# def stock_span(arr):
#     span=[]
#     for i in range(len(arr)):
#         stack=[]
#         for ele in arr[:i]:
#             stack.append(ele)
#         count=1
#         while stack:
#             if stack[-1] < arr[i]:
#                 count +=1
#                 stack.pop()
#             else:
#                 break
#         span.append(count)
#     return span

            



        




# # n=int(input('Enter length of Array'))
# # arr=[]
# # for i in range(n):
# #     arr.append(int(input('Enter Element')))
# arr1=[60,70,80,100,90,75,80,120]
# arr=[1,2,3,4,2,5]
# print(arr)
# print(stock_span(arr))




#teaches o(n) both

def stock_span(stock):
    output=[]
    output.append(1)
    span=[]
    span.append(0)
    for i in range(1,len(stock)):
        while  span and stock[span[-1]] < stock[i] :
            span.pop()
        if not span:
            output.append(i+1)
        else:
            output.append(i-span[-1])
        span.append(i)
    return output

arr1=[60,70,80,75,120]
arr=[10,10,10,10]
print(arr1)
print(stock_span(arr1))
