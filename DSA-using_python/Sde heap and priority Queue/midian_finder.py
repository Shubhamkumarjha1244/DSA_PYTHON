import heapq
class MedianFinder:       

    def __init__(self):
        self.first_half=[] #pop give largest of first half
        self.second_half=[] #pop give smallest of second half
        

    def addNum(self, num: int) -> None:
        if len(self.first_half)==len(self.second_half):
            heapq.heappush(self.first_half,-num)
            temp=-heapq.heappop(self.first_half)    #we can use heappoppush to reduce time VVVVVVVI
            heapq.heappush(self.second_half,temp)
        else:
            heapq.heappush(self.second_half,num)
            temp=heapq.heappop(self.second_half)
            heapq.heappush(self.first_half,-temp)
        


        

    def findMedian(self) -> float:

        if len(self.first_half)==len(self.second_half):
            return (-self.first_half[0]+self.second_half[0])/2
        else:return self.second_half[0]

def findMedian(arr):
    second_half=[]
    first_half=[]
    for ele in arr:
        if len(second_half)==len(first_half):
            temp=heapq.heappushpop(second_half,ele)
            heapq.heappush(first_half,-temp)
            if len(arr)%2==0:
                print((second_half[0]-first_half[0])/2,end=' ')
            else:
                print(-first_half[0],end=' ')
        else:
            temp=-heapq.heappushpop(first_half,-ele)
            heapq.heappush(second_half,temp)
            if len(arr)%2==0:
                print((second_half[0]-first_half[0])/2,end=' ')
            else:
                print(-first_half[0],end=' ') 
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
obj.addNum(5)
obj.addNum(6)
print('even',obj.findMedian())
obj.addNum(7)
print('odd',obj.findMedian())
obj.addNum(16)
print('even',obj.findMedian())


arr=[6,4,2,2,3,4]
findMedian(arr)