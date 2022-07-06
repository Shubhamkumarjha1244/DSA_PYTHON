import queue

class stack_using_single_queue:
    def __init__(self):
        self.__data=queue.Queue()
    
    def push(self,value):
        if self.isEmpty()==True:
            self.__data.put(value)
            return
        self.__data.put(value)
        c=0
        move=self.__data.qsize()
        while c <move:
            self.__data.put(self.__data.get())
            c+=1
        return
    

    def pop(self):
        if self.isEmpty()==True:
            return -500
        return  self.__data.get()
    
    def top(self):
        if self.isEmpty()==True:
            return -500
        return self.__data.queue[0]
    
    def size(self):
        return self.__data.qsize()

    def isEmpty(self):
        return self.__data.qsize() == 0
