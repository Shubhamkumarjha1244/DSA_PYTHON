def lcs(s1,s2):
    dp=[[-1 for j in range(len(s2))] for i in range(len(s1))]
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j]:
                if i+1<len(s1) and j+1<len(s2):
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=1
            else:
                if i+1<len(s1):
                    comb1=dp[i+1][j]
                else:comb1=0
                if j+1<len(s2):
                    comb2=dp[i][j+1]
                else:comb2=0
                dp[i][j]=max(comb1,comb2)
    return dp[0][0]


str1=input('Enter first string : ')
str2=input('Enter second string : ')
print(lcs(str1,str2))