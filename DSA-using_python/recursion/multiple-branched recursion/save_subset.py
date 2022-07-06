def Subset(str):
    if len(str)==0:
        output=[]
        output.append('')
        return output

    first_char=str[0]
    smaller_string=str[1:]
    smaller_subset=Subset(smaller_string)
    output=[]
    for ele in smaller_subset:
        subset=first_char+ele
        subset2=ele
        output.append(subset)
        output.append(subset2)
    return output

str='abc'
print(Subset(str))
