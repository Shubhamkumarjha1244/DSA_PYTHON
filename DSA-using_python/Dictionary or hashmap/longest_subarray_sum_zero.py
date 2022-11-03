def longest_subarray_sum_zero(arr):
    dic={}
    max_len=0
    for i in range(len(arr)):
        sum_till=sum(arr[:i+1])
        if sum_till not in dic:dic[sum_till]=i
        else:max_len=max(max_len,i-dic[sum_till])
    return max_len










arr=[95,-97,-387,-435,-5,-70,897,127,23,284]
print(longest_subarray_sum_zero(arr))