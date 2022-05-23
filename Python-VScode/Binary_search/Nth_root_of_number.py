def power(num,power):
    ans=1
    for i in range(power):
        ans=ans*num
    return ans
def nth_root(st,en,number,root):
    while en-st>1e-6:
        mid=(en+st)/2.0
        if power(mid,root)>number:
            en=mid
        if power(mid,root)<=number:
            st=mid
    return round(mid,5)












number=int(input("Enter Number"))
root=int(input("Enter root"))
print(nth_root(0,number,number,root))
