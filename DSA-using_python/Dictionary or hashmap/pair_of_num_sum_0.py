def pair_sum_zero(arr):
    dic={}
    for ele in arr:
        if -ele in dic:
            print(ele,-ele)
            dic[-ele]=-1
            dic[ele]=-1
        else:dic[ele]=1

arr=[int(ele) for ele in input().split(' ')]
pair_sum_zero(arr)