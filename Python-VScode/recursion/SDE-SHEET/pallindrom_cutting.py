
def is_pallindrom(stri,start,end):
    while start < end :
        if stri[start] != stri[end]:
            return False
        start +=1
        end -=1
    return True
def pallindrom(ind,stri,ans,output):
    if ind==len(stri):
        output.append(ans)
        return
    for i in range(ind,len(stri)):
        if is_pallindrom(stri,ind,i) is True:
            pallindrom(i+1,stri,ans+[stri[ind:i+1]],output)            

def pallindrom_partition(stri):
    output=[]
    pallindrom(0,stri,list(),output)
    return output

stri='aab'
print(pallindrom_partition(stri))

