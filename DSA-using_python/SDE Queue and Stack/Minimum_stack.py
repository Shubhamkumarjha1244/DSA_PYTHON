class minimumstack_using_2d_list:
    def __init__(self):
        self.__data=[]

    def push(self,val):
        if len(self.__data)==0:
            self.__data.append([val,val])
            return
        self.__data.append([val,min(val,self.__data[-1][1])])
        return
    def pop(self):
        if len(self.__data)==0:
            print("it's empty")
            return
        self.__data.pop()
        return
    def getMin(self):
        if len(self.__data)==0:
            print("it's empty")
            return
        return self.__data[-1][1]
    def top(self):
        if len(self.__data)==0:
            print("it's empty")
            return
        return self.__data[-1][0]

# class minimum_stack:

#     def __init__(self):
#         self.__list=[]
#         self.__min=0

#     def push(self,val):
#         if len(self.__list)==0:
#             self.__list.append(val)
#             self.__min=val
#             return
#         elif val>=self.__min:
#             self.__list.append(val)
#             return
#         else:
#             self.__list.append(2*val-self.__min) #clear at pop
#             self.__min=val
#             return


#     def pop(self):
#         if len(self.__list)==0:
#             print("it's empty")
#             return
#         temp=self.__list.pop()
#         if temp<self.__min:
#             self.__min=2*self.__min-temp #temp=self.__list.pop()=2*val-self.__min and here val is min so when we do math it gives previous min
#         return

#     def top(self):
#         if len(self.__list)==0:
#             print("it's empty")
#             return
#         if self.__list[-1]<self.__min:
#             return self.__min
#         return self.__list[-1]
#     def getMin(self):
#         if len(self.__list)==0:
#             print("it's empty")
#             return
#         return self.__min


class minimum_stack:
    def __init__(self):
        self.__data=[]
        self.__min=0
    
    def push(self,val):
        if len(self.__data)==0:
            self.__data.append(val)
            self.__min=val
            return
        if self.__min>val:
            self.__data.append(2*val-self.__min)
            self.__min=val
            return
        self.__data.append(val)

    def pop(self):
        if len(self.__data)==0:
            return 404
        if self.__min<=self.__data[-1]:
            self.__data.pop()
            return
        else:
            temp=self.__data.pop()
            self.__min=temp-(2*self.__min-temp)
            return
    def top(self):
        if len(self.__data)==0:
            return 404
        if self.__data[-1]>self.__min:
            return self.__min
        else:
            return self.__data

    def getMin(self):
        if len(self.__data)==0:
            return 404
        return self.__min

        
        

        










q=minimumstack_using_2d_list()
print(q.push(-2),q.push(0),q.push(-3),q.getMin(),q.pop(),q.top(),q.getMin())
q=minimum_stack()
print(q.push(-2),q.push(0),q.push(-3),q.getMin(),q.pop(),q.top(),q.getMin())