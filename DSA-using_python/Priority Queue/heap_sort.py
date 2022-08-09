
def heap_insertion(input,arr):
    for i in range(len(input)):
        arr.append(input[i])
        coculate_up(arr)
    return arr
def coculate_up(arr):
    i=len(arr)-1
    while i>0:
        parent=(i-1)//2
        if arr[parent]>arr[i]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
        else:
            break

def coculate_down(arr):
    i=0
    while (2*i)+1<len(arr) or (2*i)+2<len(arr):
        left=(2*i)+1
        right=(2*i)+2
        if right >= len(arr):right_val=2e6    
        else:right_val=arr[right]
        mini=min(arr[i],arr[left],right_val)
        if mini==arr[i]:break
        elif mini==arr[left]:
            arr[left],arr[i]=arr[i],arr[left]
            i=left
        elif mini==right_val:
            arr[right],arr[i]=arr[i],arr[right]
            i=right

def heap_deletion(input,arr):
    while len(arr)!=0:
        arr[0],arr[len(arr)-1]=arr[len(arr)-1],arr[0]
        input.append(arr.pop())
        coculate_down(arr)
    return input  

def heap_sort(input):
    arr=[]
    arr=heap_insertion(input,arr)
    input=[]
    input=heap_deletion(input,arr)
    return input




input=[4,6,7,1,53,5,98]
print(heap_sort(input))