def Single_element(arr):
    en=len(arr)-1
    st=0
    while st<en:
        mid=(st+en)//2
        if mid%2!=0:
            if arr[mid]==arr[mid+1]:
                en=mid
                print('en1-',en)
            else:
                st=mid+1
                print('st1-',st)
        if mid%2==0:
            if arr[mid]==arr[mid+1]:
                st=mid+1
                print('st2-',st)
            else:
                en=mid
                print('en2-',en)
    return ('ans--',arr[st])
arr=[1,1,2,3,3,4,4,8,8]
print(Single_element(arr))