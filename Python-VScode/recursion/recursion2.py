def subset(str):
    if len(str)==0:
        output=[]
        output.append('')
        return output
    
    smaller_string=str[1:]
    smaller_string_array=subset(smaller_string)


    output=[]
    for i in smaller_string_array:
        output.append(i)
        output.append(str[0]+i)
    return output


str="abcd"
print(subset(str))
    