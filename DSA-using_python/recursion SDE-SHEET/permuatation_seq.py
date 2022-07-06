# #mine approch


# def permutation(arr,ans,output):
#     if len(arr)==0:
#         output.append(ans)
#         return 

#     for i in range(len(arr)):
#         new_arr=arr[:i]+arr[i+1:]
#         new_ans=ans+[arr[i]]
#         permutation(new_arr,new_ans,output)




# def k_permutation(n,k):
#     per=list()
#     for i in range(1,n+1):
#         per.append(i)
#     output=list()
#     permutation(per,[],output)
#     output.sort()
#     stri=''
#     for i in output[k-1]:
#         stri=stri+str(i)
#     print(stri)






# n=int(input())
# k=int(input())

# k_permutation(n,k)
# def factorial(num):
#     if num==1:
#         return 1
#     return num*factorial(num-1)

# def k_permutation(k,n,stri):
#     n=n-1
#     digit=k//factorial(k-1)
#     stri=''+str(digit)
#     small_number=k%factorial(k-1)
#     k_permutation()


# def K_permutation(k,n):
#     number=list()
#     fac=1
#     for i in range(1,k):
#         number.append(i)
#         fac=fac * i
#     number.append(k)
#     ans=''
#     n=n-1

#     while True:
#         ans=ans+''+str(number[n//fac])
#         number.remove(number[n//fac])
#         if (len(number)==0):
#             break
#         n=n % fac
#         fac=fac//len(number)
#     return ans


# print(K_permutation(3,3))



def K_permutation(num,rank):
    numList=list()
    fac=1
    for i in range(1,num):
        numList.append(i)
        fac=fac * i
    numList.append(num)
    ans=''
    rank=rank-1  #for converting one to zero index

    while True:
        ans=ans+''+str(numList[rank//fac])
        numList.remove(numList[rank//fac])
        if len(numList)==0: break
        rank=rank%fac
        fac=fac//len(numList)
    return ans

print(K_permutation(4,17))

    

