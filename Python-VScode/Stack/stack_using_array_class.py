class stack:
    def __init__(self):
        self.__data=[]
    
    def push(self,item):
       self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print('hey! stack is empty')
            return
        return self.__data.pop()
    def length(self):
       return  len(self.__data)
    def top(self):
        if self.isEmpty():
            print('hey! stack is empty')
            return
        return self.__data[self.length()-1]
    def isEmpty(self):
        return self.length()==0
    
    