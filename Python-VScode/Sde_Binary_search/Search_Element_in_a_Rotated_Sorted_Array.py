def Search_element_in_rotated_sorted_array(arr,ele):
    st=0
    en=len(arr)-1
    while st<=en:
        mid=(st+en)//2
        if arr[mid]==ele:
            return mid
        if arr[st]<arr[mid]:
            if (arr[0]<=ele and arr[mid]>=ele):
                en=mid-1
                print("en1--",en)
            else:
                st=mid+1
                print("st1--",st)
        else:
           if (arr[mid+1]<=ele and arr[en]>=ele): 
               st=mid+1
               print("st2--",st)

           else:
                en=mid-1
                print("en2--",en)         
    return -1



def Search_pivot_in_rotated_sorted_array(arr):
    st=0
    en=len(arr)-1
    while st<=en:
        mid=(st+en)//2
        if arr[mid-1]>arr[mid] and arr[mid+1]>arr[mid] :
            return mid
        if arr[st]<arr[mid]:
                st=mid+1
                print("Start",st)
        else:
           en=mid-1
           print("End",en)         
    return -1
arr=[4,5,6,7,1]
ele=10
print(Search_element_in_rotated_sorted_array(arr,ele))
print(Search_pivot_in_rotated_sorted_array(arr))


        

