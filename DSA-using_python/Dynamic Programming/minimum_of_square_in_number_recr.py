import sys
def minimum_square(num,dp):
    if num==1:return 1
    i=1
    mini=sys.maxsize
    while i**2<=num:
        left_out=num-(i**2)
        if left_out==0:return 1
        if dp[left_out]==-1:dp[left_out]=minimum_square(left_out,dp)
        mini=min(mini,dp[left_out])
        i+=1
    return 1+mini
num=int(input('Enter Number'))
dp=[-1 for i in range(num+1)]
print(minimum_square(num,dp))