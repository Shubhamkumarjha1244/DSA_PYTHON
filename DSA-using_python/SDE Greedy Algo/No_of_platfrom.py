def No_of_train(n,arr,dep):
    arr.sort()
    dep.sort()
    i=0 
    j=0
    platform_required=0
    max_platfrom_required=1

    while j<n and i<n:
        if dep[j]>=arr[i]:
            i+=1
            platform_required+=1
        else:
            j+=1
            platform_required-=1
        max_platfrom_required=max(max_platfrom_required,platform_required)

    return max_platfrom_required



    











# n=int(input('No of train'))
# arr=[int(ele) for ele in input().split(' ')]
# dep=[int(ele) for ele in input().split(' ')]
n=6
arr=[900,945,955,1100,1500,1800]
dep=[920,1200,1130,1150,1900,2000]
print(No_of_train(n,arr,dep))
