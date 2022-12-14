
def edit_distance(str1,str2):
    dp= [[-1 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(len(str1)+1):dp[i][0]=i
    for j in range(len(str2)+1):dp[0][j]=j
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[-1][-1]



str1=input("Enter String one")
str2=input("Enter String Two")
# str1='horse'
# str2='ros'
print(edit_distance(str1,str2))