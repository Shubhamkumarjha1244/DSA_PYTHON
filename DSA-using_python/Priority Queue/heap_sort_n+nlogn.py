def heap_sort_n_nlogn(input):
    make_heap(input)
    take_from_heap(input)
    return input


def down_heapify_from(input,i):
    leng=len(input)
    while (2*i+1)<leng and (2*i+2)<leng:
        left=(2*i+1)
        if (2*i+2)>=leng:right_val=1e12
        else:right_val=input[2*i+2]
        mini=min(input[left],right_val,input[i])
        if mini==input[i]:break
        elif mini==input[left]:
            input[i],input[left]=input[left],input[i]
            i=left
        elif mini==right_val:
            input[i],input[2*i+2]=input[2*i+2],input[i]
            i=2*i+2

def down_heapyfy_till(input,end):
    i=0
    while (2*i+1)<end or (2*i+2)<end:
        left=2*i+1
        if (2*i+2)>=end:right_val=2e10
        else:right_val=input[2*i+2]
        mini=min(input[left],input[i],right_val)
        if mini==input[i]:break
        elif mini==input[left]:
            input[i],input[left]=input[left],input[i]
            i=left
        elif mini==right_val:
            input[i],input[2*i+2]=input[2*i+2],input[i]
            i=(2*i+2)
#we can make heap_down in one function
def make_heap(input):
    non_leaf=len(input)//2
    for i in range(non_leaf-1,-1,-1):
        down_heapify_from(input,i)
    return input

def take_from_heap(input):
    leng=len(input)
    for i in range(len(input)):
        input[0],input[leng-1-i]=input[leng-1-i],input[0]
        down_heapyfy_till(input,leng-1-i)
    return input



input=[4,6,7,1,10000,-12332,53,5,98,98]
print(heap_sort_n_nlogn(input))