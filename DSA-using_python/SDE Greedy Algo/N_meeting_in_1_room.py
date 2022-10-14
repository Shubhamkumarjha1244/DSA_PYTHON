import heapq
def max_meeting_in_one_room(n,start,end):
    meeting=[]
    ans=[]
    for i in range(n):
        meeting.append((end[i],start[i],i+1))
    meeting.sort()
    print(meeting)
    end=0
    while len(meeting)!=0:
        meet=meeting[0]
        meeting=meeting[1:]
        if end>meet[1]:continue
        end=meet[0]
        ans.append(meet[2])
    return ans     
    



# n=int(input("total meeting"))
# start=[ele for ele in input().split(' ')]
# end=[ele for ele in input().split(' ')]
n=6
start=[1,3,0,5,8,5]
end=[2,4,5,7,9,9]
print(max_meeting_in_one_room(n,start,end))