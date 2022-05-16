class minimum_using_2d_list:
    def __init__(self):
        self.__data=[]

    def push(self,val):
        if len(self.__data)==0:
            self.__data.append([val,val])
            return
        self.__data.append([val,min(val,self.__data[-1][1])])
        return
    def pop(self):
        self.__data.pop()
        return
    def getMin(self):
        return self.__data[-1][1]
    def top(self):
        return self.__data[-1][0]


q=minimum_using_2d_list()
print(q.push(-2),q.push(0),q.push(-3),q.getMin(),q.pop(),q.top(),q.getMin())