def pair_sum_zero(arr):
    dic={}
    for ele in arr:
        if -ele in dic:
            print(ele,-ele)
            dic[-ele]-=1
            if dic[-ele]==0:dic.pop(-ele)
        else:
            if ele not in dic:
                dic[ele]=1
            else:
                dic[ele]+=1


arr=[int(ele) for ele in input().split(' ')]
pair_sum_zero(arr)