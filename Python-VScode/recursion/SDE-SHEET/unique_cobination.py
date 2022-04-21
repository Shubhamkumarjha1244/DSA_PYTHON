# def unique_combination(pos,arr,target,ans,out):
#     if target==0:
#         print(ans)
#         return
#     for i in range(pos,len(arr)) :
#         if i > pos and arr[i]==arr[i-1] :
#             continue
#         if arr[i] > target:
#             break
#         ans.append(arr[i])
#         unique_combination(i+1,arr,target-arr[i],ans,out)
#         ans.pop()
# def print_unique(arr,target):
#     output=[]
#     arr.sort()
#     unique_combination(0,arr,target,list(),output)
#     print(output)
#     return
# can=[10,1,2,7,6,1,5]
# target=8
# print_unique(can,target)
def combi(pos,arr,target,ans):
    if target==0:
        print(ans)
        return
    for i in range(pos,len(arr)):
        if i >pos and arr[i]==arr[i-1]:
            continue
        if arr[i] > target:
            break
        ans.append(arr[i])
        combi(i+1,arr,target-arr[i],ans)
        ans.pop()

def print_unique(arr,target):
    arr.sort()
    combi(0,arr,target,list())

can=[10,1,2,7,6,1,5]
target=8
print_unique(can,target)