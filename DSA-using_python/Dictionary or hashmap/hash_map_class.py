class hashnode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class hashmap:
    def __init__(self):
        self.bucket_size=10
        self.bucket=[None for i in range(self.bucket_size)]
        self.count=0

    def size(self):
        return self.count


    def rehashing(self):
        self.count=0
        temp=self.bucket_size
        temp_bucket=self.bucket
        self.bucket_size=2*temp
        self.bucket=[None for i in range(self.bucket_size)]
        for bucket in temp_bucket:
            head=bucket
            while head:
                self.updateORinsert(head.key,head.value)
                head=head.next
        


    def compress(self,hc):
        return abs(hc)%self.bucket_size
    def updateORinsert(self,key,value):
        hc=hash(key)   #hashing
        bucket_index=self.compress(hc)    # compression of hashed index
        head=self.bucket[bucket_index]
        while head:        #update
            if head.key==key:
                head.value=value
                return
            head=head.next
        newNode=hashnode(key,value) #insert 
        newNode.next=self.bucket[bucket_index]
        self.bucket[bucket_index]=newNode
        self.count+=1
        #rehashing
        self.load_factor=self.count/self.bucket_size
        if self.load_factor>=0.7:self.rehashing()  #rehashing



    def get_value(self,key):
        hc=hash(key)
        index=self.compress(hc)
        head=self.bucket[index]
        while head:
            if head.key==key:
                return head.value
            head=head.next
        return None




    def remove(self,key):
        hc=hash(key)
        index=self.compress(hc)
        head=self.bucket[index]
        prev=None
        if head.key==key:
            self.bucket[index]=head.next
            return head.value
        while head:
            if head.key==key:
                prev.next=head.next
                return head.value
            prev=head
            head=head.next
        return None

m=hashmap()
m.updateORinsert('shubham',1)   
print(m.get_value('shubham'))
m.updateORinsert('shubham',4)   
print(m.get_value('shubham'))      
m.updateORinsert('shubham1',42)   
print(m.get_value('shubham')) 
print(m.get_value('shubham1')) 
m.updateORinsert('shubham1',5) 
print(m.get_value('shubham1')) 
print("delete")
print(m.remove('shubham1'))
print(m.get_value('shubham1'))
print(m.get_value('shubham'))

for i in range(400):
    m.updateORinsert('abc'+str(i),i)
    print(m.load_factor)
