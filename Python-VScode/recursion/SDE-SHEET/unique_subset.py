# def unique(pos,arr,ans,out):
#     print(ans)
#     for i in range(pos,len(arr)) :
#         if i !=pos and arr[i]==arr[i-1]:
#             continue
#         ans.append(arr[i])
#         unique(i+1,arr,ans,out)
#         ans.pop()

# def print_unique(arr):
#     output=[]
#     arr.sort()
#     unique(0,arr,list(),output)
    
#     return
# arr=[1,2,2]
# print_unique(arr)

def unique_subset(pos,arr,ans,output):
    output.append(list(ans))
    for i in range(pos,len(arr)):
        if i > pos and arr[i]==arr[i-1]:
            continue
        ans.append(arr[i])
        print(output)
        unique_subset(i+1,arr,ans,output)
        ans.pop()
    



def printsubset(arr):
    arr.sort()
    output=list()
    unique_subset(0,arr,list(),output)
    print()
    print(output)
    return output

arr=[1,2,2]
print(printsubset(arr))
