def max_no_meeting(n,start,finish):
    meeting=[]
    for i in range(n):
        meeting.append((start[i],finish[i]))
    meeting.sort(key=lambda a:a[1])
    end=meeting[0][1]
    ans=1
    for meet in meeting[1:]:
        if meet[0]>=end:
            ans+=1
            end=meet[1]
    return ans


n=4
act_start=[1,6,2,4]
act_end=[2,7,5,8]
print(max_no_meeting(n,act_start,act_end))