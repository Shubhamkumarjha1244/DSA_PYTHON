def Extract_string(s):
    dic={}
    for stri in s:
        if stri not in dic:dic[stri]=1
    return ''.join(dic)    


s=input('Enter String--- ')
print(Extract_string(s))