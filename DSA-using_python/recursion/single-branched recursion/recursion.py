def Subset(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output

    substring=s[1:]
    substringarray=Subset(substring)

    output=[]
    for sub in substringarray:
        output.append(sub)
    for sub in substringarray:
        output.append(sub+s[0])
    
    return output


s="a"
print(Subset(s))






s=input("Enter String")
print()



    



