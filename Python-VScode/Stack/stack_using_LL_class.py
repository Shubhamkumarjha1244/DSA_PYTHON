from node_class import Node
class stack:
    def __init__(self):
        self.__head=None
        self.__count=0

    def push(self,value):
        node=Node(value)
        node.next=self.__head
        self.__head=node
        self.__count=self.__count+1

    def pop(self):
        if self.isEmpty() is True:
            print('hey,Stack is empty')
            return
        data=self.__head.data
        self.__head=self.__head.next
        self.__count=self.__count-1
        return data
    
    def top(self):
        if self.isEmpty() is True:
            print('hey,Stack is empty')
            return
        return self.__head.data


    def length(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0 
        


        


