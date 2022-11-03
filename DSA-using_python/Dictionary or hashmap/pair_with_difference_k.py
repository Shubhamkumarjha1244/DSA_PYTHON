def pair_with_difference(arr,diff):
    dic={}
    ans=0
    for ele in arr:
        if ele not in dic:dic[ele]=1
        else:dic[ele]+=1
    for ele in arr:
        if ele-diff in dic:
            ans+=(dic[ele]*dic[ele-diff])
            print(ele-diff,ele)
        if ele+diff in dic:
            ans+=(dic[ele]*dic[ele+diff])
            print(ele+diff,ele)
        dic[ele]=0 
    return ans


arr=[int(ele) for ele in input('enter arr : ').split(' ')]
diff=int(input('Enter difference : '))
print(pair_with_difference(arr,diff))