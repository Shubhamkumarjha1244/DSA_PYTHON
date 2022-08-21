
def heap_insertion(input):
    for i in range(len(input)-1,-1,-1):
        coculate_up(input,i)
    return input
def coculate_up(arr,i):
    while i>0:
        parent=(i-1)//2
        if arr[parent]>arr[i]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
        else:break
    

def coculate_down(arr,end):
    i=0
    while (2*i)+1<end or (2*i)+2<end:
        left=(2*i)+1
        right=(2*i)+2
        if right >= end:right_val=2e6    
        else:right_val=arr[right]
        mini=min(arr[i],arr[left],right_val)
        if mini==arr[i]:break
        elif mini==arr[left]:
            arr[left],arr[i]=arr[i],arr[left]
            i=left
        elif mini==right_val:
            arr[right],arr[i]=arr[i],arr[right]
            i=right

def heap_deletion(input):
    for i in range(len(input)):
        input[0],input[len(input)-1-i]=input[len(input)-1-i],input[0]
        coculate_down(input,len(input)-1-i) 
    return input

def heap_sort(input):
    input=heap_insertion(input)
    print('hi',input)
    input=heap_deletion(input)
    return input




input=[4,6,7,1,10000,53,5,98,98]
print(heap_sort(input))