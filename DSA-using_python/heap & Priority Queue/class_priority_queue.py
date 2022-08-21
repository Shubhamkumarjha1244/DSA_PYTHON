from cmath import inf


class priorityNode:
    def __init__(self,val,priority):
        self.data=val
        self.priority=priority

    
class PriorityQueue_min:
    def __init__(self):
        self.arr=[]
    def getsize(self):
        return len(self.arr)
    def percolate_up(self):
        pos=len(self.arr)-1
        while pos>0:
            parent=(pos-1)//2
            if self.arr[parent].priority>self.arr[pos].priority:
                self.arr[pos],self.arr[parent]=self.arr[parent],self.arr[pos]
                pos=parent
            else:break

    def percolate_down(self):
        top=0
        while ((2*top)+1)<len(self.arr) or ((2*top)+2)<len(self.arr):
            top_node=self.arr[top]
            left_node=self.arr[(2*top)+1]
            if ((2*top)+2)<len(self.arr):right_node=self.arr[(2*top)+2]
            else:right_node=priorityNode(None,2e32)
            min_priority=min(top_node.priority,left_node.priority,right_node.priority)
            if min_priority==top_node.priority:break
            for ele in [(2*top)+1,(2*top)+2]:
                if min_priority==self.arr[ele].priority:
                    min_priority=ele
                    break
            self.arr[top],self.arr[min_priority]=self.arr[min_priority],self.arr[top]
            if min_priority==(2*top)+1:top=(2*top)+1
            if min_priority==(2*top)+2:top=(2*top)+2
        

    def insert(self,node):
        self.arr.append(node)
        self.percolate_up()

    def delete_min(self):
        if len(self.arr)==0:return 404
        self.arr[0],self.arr[len(self.arr)-1]=self.arr[len(self.arr)-1],self.arr[0]
        temp=self.arr.pop().data
        self.percolate_down()
        return temp

    def is_empty(self):
        return len(self.arr)==0

    def get_min_priority(self):
        if self.is_empty():return 404
        return self.arr[0].data

    # def print(self):
    #     for ele in self.arr:
    #         print(ele.data,ele.priority,end='->')


class PriorityQueue_max:
    def __init__(self):
        self.arr=[]
    def getsize(self):
        return len(self.arr)
    def percolate_up(self):
        pos=len(self.arr)-1
        while pos>0:
            parent=(pos-1)//2
            if self.arr[parent].priority<self.arr[pos].priority:
                self.arr[pos],self.arr[parent]=self.arr[parent],self.arr[pos]
                pos=parent
            else:break

    def percolate_down(self):
        top=0
        while ((2*top)+1)<len(self.arr) or ((2*top)+2)<len(self.arr):
            top_node=self.arr[top]
            left_node=self.arr[(2*top)+1]
            if ((2*top)+2)<len(self.arr):right_node=self.arr[(2*top)+2]
            else:right_node=priorityNode(None,-2e32)
            max_priority=max(top_node.priority,left_node.priority,right_node.priority)
            if max_priority==top_node.priority:break
            for ele in [(2*top)+1,(2*top)+2]:
                if max_priority==self.arr[ele].priority:
                    max_priority=ele
                    break
            self.arr[top],self.arr[max_priority]=self.arr[max_priority],self.arr[top]
            if max_priority==(2*top)+1:top=(2*top)+1
            if max_priority==(2*top)+2:top=(2*top)+2
   
    def insert(self,node):
        self.arr.append(node)
        self.percolate_up()

    def delete_max(self):
        if len(self.arr)==0:return 404
        self.arr[0],self.arr[len(self.arr)-1]=self.arr[len(self.arr)-1],self.arr[0]
        temp=self.arr.pop().data
        self.percolate_down()
        return temp

    def is_empty(self):
        return len(self.arr)==0

    def get_max_priority(self):
        if self.is_empty():return 404
        return self.arr[0].data




















a1=priorityNode(1,20)
a2=priorityNode(2,30)
a3=priorityNode(3,70)
a4=priorityNode(4,10)
a5=priorityNode(5,90)
a6=priorityNode(6,65)

min_priority_queue=PriorityQueue_min()
max_priority_queue=PriorityQueue_max()

min_priority_queue.insert(a1)
min_priority_queue.insert(a2)
min_priority_queue.insert(a3)
min_priority_queue.insert(a4)
min_priority_queue.insert(a5)
min_priority_queue.insert(a6)

max_priority_queue.insert(a1)
max_priority_queue.insert(a2)
max_priority_queue.insert(a3)
max_priority_queue.insert(a4)
max_priority_queue.insert(a5)
max_priority_queue.insert(a6)
print("-----size-----")
print(max_priority_queue.getsize())
print(min_priority_queue.getsize())
print("----end----")
print(min_priority_queue.get_min_priority())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())
print(min_priority_queue.delete_min())

print('----max_priority_queue----')

print(max_priority_queue.get_max_priority())
print('max')
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
print(max_priority_queue.delete_max())
