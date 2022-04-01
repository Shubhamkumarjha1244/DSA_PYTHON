def geometric_sum(n:float):
    if n==0:
        return 1
    return (1/(2**n))+geometric_sum(n-1)


n=4
print(geometric_sum(n))


def check_pallindrom(str,st,en):

    if st>en:
        return True
    if str[st]!=str[en]:
        return False
    return check_pallindrom(str,st+1,en-1)

str="123321"
print(check_pallindrom(str,0,5))

def sum_of_number(num):
    if num == 0:
        return 0
    return num + sum_of_number(num-1)

num=990
print(sum_of_number(num))


def multiply(num1,num2):
    if num1==0 or num2==0:
        return 0
    return num1+multiply(num1,num2-1)

n1=5
n2=10
print(multiply(1,34))
