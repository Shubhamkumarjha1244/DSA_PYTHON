def check_pallindrom(num,st,en):
    if st>=en:
        return True
    if num[st]!=num[en]:
        return False
    return check_pallindrom(num,st+1,en-1)
def pallindrom(num):
    return check_pallindrom(num,0,len(num)-1)

def replace(stri,st):
    if st>=len(stri):
        return stri
    if stri[:2]=='pi':
        stri='3.14'+replace(stri[2:],st+2)
    stri=stri[0]+replace(stri[1:],st+1)
    



def replacePi(stri):
    return replace(stri,0)


num=[1,2,2,1,3]
print(pallindrom(num))

stri='pipipi'
print(replacePi(stri))



