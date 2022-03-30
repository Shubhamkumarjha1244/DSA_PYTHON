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



def binary_search_mine(arr,key):       #array is deflaut sorted
    if len(arr)==0:
        return False
    mid=(int(len(arr)/2))
    if arr[mid] == key:
        return True
    if key > arr[mid]:
       return binary_search_mine(arr[mid+1:],key)
    else:

        return binary_search_mine(arr[:mid],key)

    
    
def binary_search(arr,key,startindex,endindex):       #array must be is deflaut sorted
    if startindex > endindex:
        return -1
    mid=(startindex+endindex)//2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binary_search(arr,key,mid+1,endindex)
    else:
        return binary_search(arr,key,startindex,mid-1)
def merge(arr1,arr2,arr):
        i=0
        j=0
        k=0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >arr2[j] :
                arr[k]=arr2[j]
                j+=1
                k+=1
            else:
                arr[k]=arr1[i]
                i+=1
                k+=1
        while  i < len(arr1):
            arr[k]=arr1[i]
            i+=1
            k+=1
        
        while j < len(arr2):
            arr[k]=arr2[j]
            j+=1
            k+=1
        return arr

def merge_sort(arr):
    if len(arr)==1 or len(arr)==0:
        return
    mid=len(arr)//2 #to find middle using floor division
    a1=arr[:mid]
    a2=arr[mid:]
    merge_sort(a1)
    merge_sort(a2)
    return merge(a1,a2,arr)

def binary_search_practice(arr,key,st,en):
    if st > en:
        return -1
    mid =(st+en)//2
    if arr[mid] == key :
        return mid
    elif arr[mid]>key:
        return binary_search_practice(arr,key,st,mid-1)
    else:
        return binary_search_practice(arr,key,mid+1,en)
    








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
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
key=6
print(arr,'---',binary_search_mine(arr,key))
print(arr,'---practice---',binary_search_practice(arr,1,0,11))
arr1=[2,1,3,4,5,6,7,8,9,10,12,11]
arr2=merge_sort(arr1)
print('unsorted array---',arr1,'sorted array---',arr2)