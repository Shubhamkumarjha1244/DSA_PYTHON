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
    print(ans,end=' , ')
    for i in range(pos,len(arr)):
        if i > pos and arr[i]==arr[i-1]:
            continue
        ans.append(arr[i])
        unique_subset(i+1,arr,ans,output)
        ans.pop()
    



def printsubset(arr):
    arr.sort()
    output=list()
    unique_subset(0,arr,list(),output)

arr=[1,2,2]
printsubset(arr)
