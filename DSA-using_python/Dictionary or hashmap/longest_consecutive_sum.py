def longest_consecutive(arr):
    max_st=[]
    max_len=0
    dic={}
    st_dic={}
    for ele in arr:dic[ele]=True

    for ele in dic:
        temp=ele
        length=1
        st=ele
        dic[ele]=False
        while (ele+1) in dic and dic[ele+1]==False:
                length+=1
                dic[ele+1]=False
                ele+=1
        ele=temp
        while (ele-1) in dic and dic[ele-1]==False:
                length+=1
                st=ele-1
                dic[ele-1]=False
                ele-=1
        if length not in st_dic:st_dic[length]=[]
        st_dic[length].append((st,arr.index(st)))
        max_len=max(max_len,length)
    st_dic[max_len].sort(key=lambda a:a[1])
    return st_dic[max_len][0][0],st_dic[max_len][0][0]+max_len-1
    



    
        
                

# arr=[int(ele) for ele in input('Enter arr value').split(' ')]
arr=[2,12,9,16,10,5,3,20,25,11,1,8,6]
arr1=[3,7,2,1,9,8,41]
arr2=[15,24,23,12,19,11,16]
print(longest_consecutive(arr))