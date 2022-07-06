def permutation(str,ans):
    if len(str)==0:
        print(ans)
        return
    
    for i in range(len(str)):
        new_ans=ans+str[i]
        new_str=str[:i]+str[i+1:]   #vvi
        permutation(new_str,new_ans)



permutation('aab','')
