# from queue import Queue
# def min_time_rotten(arr):
#     total_orange=0
#     q=Queue()
#     time=0
#     final_rotten_orange=0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j]==2:
#                 q.put([i,j])
#             if arr[i][j] !=0:
#                 total_orange+=1
#     x=[0,0,1,-1]
#     y=[1,-1,0,0]
#     while q.empty()==False:
#         size=q.qsize()
#         final_rotten_orange+=size
#         for i in range(size):
#             temp=q.get()
#             for i in range(4):
#                 x_co=temp[0]+x[i]
#                 y_co=temp[1]+y[i]
#                 if x_co<0 or y_co<0 or x_co>len(arr)-1 or y_co>len(arr[0])-1 or arr[x_co][y_co]==0 or arr[x_co][y_co]==2:
#                     continue
#                 arr[x_co][y_co]=2
#                 q.put([x_co,y_co])
#         if q.qsize()!=0:
#             time+=1
#     if final_rotten_orange==total_orange: return time
#     else: return -1

from queue import Queue


def rotten_orange(arr):
    q=Queue()
    total_oranges=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==2:
                q.put([i,j])
            if arr[i][j] !=0:
                total_oranges+=1
    rotten=0
    time=0
    x=[0,0,1,-1]
    y=[1,-1,0,0]
    while q.qsize()!=0:
        rotten+=q.qsize()
        for i in range(q.qsize()):
            temp=q.get()
            for i in range(4):
                x_co=temp[0]+x[i]
                y_co=temp[1]+y[i]
                if x_co<0 or y_co<0 or x_co>len(arr)-1 or y_co>len(arr[0])-1 or arr[x_co][y_co]==0 or arr[x_co][y_co]==2:
                    continue
                arr[x_co][y_co]=2
                q.put([x_co,y_co])
        if q.qsize() !=0 :
            time+=1
    if total_oranges==rotten:return time
    else:return -1







            








arr=[[2,1,1],[1,1,0],[0,1,1]]
print(rotten_orange(arr))