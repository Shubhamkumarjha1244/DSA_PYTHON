
class queue:
    def __init__(self):
        self.__data=[]
        self.__count=0
        self.__front=0
    def enqueue(self,value):
        self.__data.append(value)
        self.__count +=1
        return value
    def dequeue(self):
        if self.__count==0:
            return -1
        ele=self.__data[self.__front]
        self.__front +=1
        self.__count -=1
        return ele

        

    def size(self):
        return self.__count
    def front(self):
        if self.__count==0:
            return -1
        return self.__data[self.__front]
    def isEmpty(self):
        return self.size()==0


