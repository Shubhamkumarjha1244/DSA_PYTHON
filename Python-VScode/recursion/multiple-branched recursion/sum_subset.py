def sum_subset(num):

    if len(num)==0:
        return 0
    
    digit=num[0]
    smaller_number=num[1:]
    smaller_number_sum=sum_subset(smaller_number)
    sum=smaller_number_sum+smaller_number_sum+digit
    return sum
a=[2,3]
print(sum_subset(a))