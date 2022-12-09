def max_prod_arr(arr):
    front=1
    back=1
    for ele in arr:
        if ele==0:front=1
        else:front*=ele
    for ele in arr[::-1]:
        if ele==0:back=1
        else:back*=ele
    return max(front,back)


arr=[int(ele) for ele in input("Enter array value : ").split(' ')]
print(max_prod_arr(arr))
