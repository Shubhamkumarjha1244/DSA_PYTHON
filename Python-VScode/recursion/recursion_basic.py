def print_first_n_natural_number(n:int):
    if n==1:
        print(n)
        return
    print(n)
    print_first_n_natural_number(n-1)


def fabonaciSeries(num:int):
    if num ==1:
        return 1
    if num == 0:
        return 0
        
    return fabonaciSeries(num-1)+fabonaciSeries(num-2)

def sum_of_list(arr):
    if len(arr)==0:
        return 0
    return arr[0]+sum_of_list(arr[1:])





def replace_char(str,charA,charB):
    if len(str)==0:
        return str

    smaller_str=str[1:]
    if str[0]==charA[0]:
        str=charB[0]+replace_char(smaller_str,charA,charB)
    else:
        str=str[0]+replace_char(smaller_str,charA,charB)
    return str

def remove_char(str,charA):
    if len(str)==0:
        return str

    smaller_str=str[1:]
    if str[0]==charA[0]:
        str=remove_char(smaller_str,charA)
    else:
        str=str[0]+remove_char(smaller_str,charA)
    return str
  

    
def replace_pi(str):
    if len(str)==0 or len(str)==1:
        return str
    if str[:2]=='pi':
        str='3.14'+replace_pi(str[2:])
    else:
        str=str[0]+replace_pi(str[1:])
    return str

def unique_array(arr):                              #all unique element in array
    if len(arr)==0 or len(arr)==1:   
        return arr
    if arr[0]==arr[1]:
        arr=unique_array(arr[1:])
    else:
        arr=[arr[0]] + unique_array(arr[1:])
    return arr



    
    








input=30
print_first_n_natural_number(input)
print("fabonaci-Series --",fabonaciSeries(input))
arr=[1,2,3,4,5,6,7,8,9,10]
print("sum of array  --",sum_of_list(arr))
str='aabbxxcvxxd'
charA='x'
charB='-'
print(str,replace_char(str,charA,charB))
print(str,remove_char(str,charA))
str='pighdppigsdhjpifssfdpi'
print(str,'\n',replace_pi(str))
arr=[1,1,2,3,4,4,4,5,6,6]
print(arr,'---',unique_array(arr))