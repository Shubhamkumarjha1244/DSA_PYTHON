def chuta_kar(n):
    denominations=[1000,500,100,50,20,10,5,2,1]  #before denomination
    ans=0
    for note in denominations:
        if n>=note:
            no_of_note=n//note
            n-=no_of_note*note
            ans+=no_of_note
            if n<=0:return ans
n=int(input('Enter Amount'))
print(chuta_kar(n))