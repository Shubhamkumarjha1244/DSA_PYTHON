def subset_number(num,ans):
    if len(num)==0:
        print(ans)
        return
    subset_number(num[1:],ans)
    new_ans=ans+[num[0]]
    subset_number(num[1:],new_ans)



n=[15,20,12]
subset_number(n,[])
