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


def star_in_string(str):
    if len(str)==0 or len(str)==1:
        return str
    elif str[0]==str[1]:
        return str[0]+'*'+star_in_string(str[1:])
    else:
        return str[0]+star_in_string(str[1:])

s='aaaabbbbcccc'
print(star_in_string(s))



def count_zero(num):
    if int(num/10)==0:
        return 1
    elif n%10 ==0:
        return 1+count_zero(int(num/10))
    else:
        return count_zero(int(num/10))


num=100
print(count_zero(num))
print(1/10)


def stair_problem(steps):
    if steps==1:
        return 1
    elif steps==2:
        return 2
    elif steps==3:
        return 4
    
    return stair_problem(steps-1)+stair_problem(steps-2)+stair_problem(steps-3)
    
n=10
print(stair_problem(n))