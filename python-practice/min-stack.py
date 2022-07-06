
class min_stack:
    def __init__(self):
        self.arr=[]
        self.min=-1

    def push(self,val):
        if len(self.arr)==0:
            self.arr.append(val)
            self.min=val
            return
        if val<self.min:
            self.arr.append(2*val-self.min)
            self.min=val
            return
        self.arr.append(val)
    
    def pop(self):
        if len(self.arr)==0:return 501
        if self.min>self.arr[-1]:
            self.min=(2*self.min)-self.arr.pop()
            return
        self.arr.pop()
    def minimum(self):
        return self.min
    def print(self):
        print(self.arr)
        print(self.min)


st=min_stack()



        
        