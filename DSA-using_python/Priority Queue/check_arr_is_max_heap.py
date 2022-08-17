
def check_max_heap(arr):
     '''kyuki heap arr format me hai to woh complete binary tree ka format ka condition 
     pura karta to apn sirf second property heap order property check karege'''
     leng=len(arr)
     for i in range(len(arr)-1,0,-1):
        parent=(i-1)//2
        if arr[parent]<arr[i]:
            return False
     return True
            
arr=[int(ele) for ele in  input().split(' ')]
print(check_max_heap(arr))