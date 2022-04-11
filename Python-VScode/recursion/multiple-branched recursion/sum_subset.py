def sum_subset(num):

    if len(num)==0:
        output=[]
        sum=0
        output.append(sum)
        return
    
    digit=num[0]
    smaller_number=num[1:]
    smaller_number_sum=sum_subset(smaller_number)
    output=[]
    sum=0
    output.append(sum)
    for ele in smaller_number_sum:
        sum_notinclude=ele
        output.append(sum_notinclude)

    for ele in smaller_number_sum:
        sum_include=ele+num[0]
        output.append(sum_include)
    return output
a=[2,3]
sum_subset(a)