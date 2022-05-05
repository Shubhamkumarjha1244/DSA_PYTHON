class queue:

    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    
    def enqueue(self,value):                 #PUT
        while len(self.__stack1)>0:
            self.__stack2.append(self.__stack1.pop())
        self.__stack1.append(value)
        while len(self.__stack2)>0:
            self.__stack1.append(self.__stack2.pop())
        return value
    def dequeue(self):                #OUT
        if self.isEmpty()==True:
            return 505
        return self.__stack1.pop()
        

    def front(self):                   
        if self.isEmpty()==True:
            return 505
        return self.__stack1[-1]

    def size(self):
        return len(self.__stack1)

    def isEmpty(self):
        return len(self.__stack1)==0
