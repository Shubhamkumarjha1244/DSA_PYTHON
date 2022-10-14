
def fractional_knapsack(limit_weight,value,weight):
    arr=[]
    for i in range(len(value)):
        arr.append([value[i]/weight[i],value[i],weight[i]])
    arr.sort(key=lambda a:a[0])
    count=0
    ans=0
    while limit_weight>0:
        var=arr.pop()
        weight=var[2]
        value=var[1]
        ratio=var[0]
        if weight<=limit_weight:
            ans+=value
            limit_weight-=weight
        else:
            fractional_weight=ratio*limit_weight
            ans+=(limit_weight/weight)*value
            limit_weight-=fractional_weight
    return ans


limit_weight=50
value=[100,60,120]
weight=[20,10,30]
print(fractional_knapsack(limit_weight,value,weight))