from node import node


class queue:
    def __init__(self):
        self.__count=0
        self.__head=None
        self.__tail=None
        
    def enqueue(self,val):
        if self.__head is None:
            self.__head=node(val)
            self.__tail=self.__head
            self.__count +=1
            return val
        self.__tail.next=node(val)
        self.__tail=self.__tail.next
        self.__count +=1
        return val
    def dequeue(self):
        if not self.__head:
            return -1
        temp=self.__head.data
        self.__head=self.__head.next
        self.__count -=1
        return temp
    def size(self):
        return self.__count
    def front(self):
        if not self.__head:
            return -1
        return self.__head.data
    def isEmpty(self):
        return self.__count==0

        