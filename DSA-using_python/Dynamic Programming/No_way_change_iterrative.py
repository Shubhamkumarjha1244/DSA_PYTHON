def change_irr(domination,value):
    dp=[i for i in range(value+1)]
    domination.sort()
    dp[0]=0
    for i in range(1,value+1):
        ways=0
        for ele in domination:
            if i-ele>=0:ways+=(1+dp[i-ele])
        dp[i]=ways
    return dp[value]


domination=[1,2,3,4,5,6]
value=int(input('Enter Value  : '))
print(change_irr(domination,value))