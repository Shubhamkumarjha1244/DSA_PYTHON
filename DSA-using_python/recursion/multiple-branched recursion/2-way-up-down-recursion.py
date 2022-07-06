def fact(num):     #first we are going to base case then we are doing movement upwArd
    if num==1:
        return 1
    return num*fact(num-1)

n=20
print(fact(n))


def fact_print(n,i): #we are going down to base case with making i as per our requirement ,no need to coming back again
    if n==1:
        print(i)
        return
    i=i*n
    return fact_print(n-1,i)

n=20
fact_print(n,1)




def minval(arr):
    if len(arr)==1:
        return arr[0]
    return min(arr[0],minval(arr[1:]))


arr=[1,2,3,754,46,4,6645,345,-5434,-6543,-543,0,-111]
print(minval(arr))

def minvalprint(arr,mini=10**4):
    if len(arr)==1:
        mini=min(arr[0],mini)
        print(mini)
        return
    mini=min(mini,arr[0])
    minvalprint(arr[1:],mini)

minvalprint(arr)

    