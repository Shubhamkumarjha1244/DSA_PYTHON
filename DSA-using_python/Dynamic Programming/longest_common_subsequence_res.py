def lcs(i,j,s1,s2):
    if i>=len(s1) or j>=len(s2):
        return 0
    if s1[i]==s2[j]:
        if dp[i][j]!=-1:return dp[i][j]
        dp[i][j]=1+lcs(i+1,j+1,s1,s2)
        return dp[i][j]
    if dp[i][j]!=-1:return dp[i][j]
    dp[i][j]=max(lcs(i+1,j,s1,s2),lcs(i,j+1,s1,s2))
    return dp[i][j]
str1=input('Enter first string')
str2=input('Enter second string')
small_str_len=min(len(str1),len(str2))
dp=[[-1 for i in range(len(str1))] for i in range(len(str2))]
print(lcs(0,0,str1,str2))
