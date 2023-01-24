import collections 
import heapq 

class Node:
    def __init__(self,count):
        self.name=None
        self.count=count
        self.left=None
        self.right=None
    def __lt__(self,other):
        return self.count < other.count
    
    def __eq__(self,other):
        return self.count == other.count




class huffman_coding:
    def __init__(self):
        self.Count=None
        self.heap=[]
        self.code={}
        self.encode_txt=''
        self.decode={}
    
    def coding(self,root,s):   #for putting new code in freq dic
        if root.count==None:return
        if root.name!=None:
            self.code[root.name]=s
            return
        self.coding(root.left,s+'0')
        self.coding(root.right,s+'1')

    def Compression(self,s):
        self.Count=collections.Counter(s)  #for counting freq
        

        for key in self.Count:  #for making heap using freq
            value,count=key,self.Count[key]
            node=Node(count)
            node.name=value
            heapq.heappush(self.heap,node)
        
        
        
        while len(self.heap)!=1:    #for making Binary Tree
            small_1=heapq.heappop(self.heap)
            small_2=heapq.heappop(self.heap)
            print(small_1.count,small_2.count)
            sum=small_1.count+small_2.count
            root=Node(sum)
            root.left=small_2
            root.right=small_1
            heapq.heappush(self.heap,root)
        

        

        self.coding(self.heap[0],'')  

        for ele in s:               #convert txt in encoded txt
            self.encode_txt+=self.code[ele]

        return self.encode_txt




    def decompress(self,s):
        for key in self.code:
            self.decode[self.code[key]]=key
        decode_txt=''
        chk=''
 
        for str in s:
            chk+=str
            if chk in self.decode:
                decode_txt+=self.decode[chk]
                chk=''
        return decode_txt
            












str=('a'*30)+('b'*10)+('c'*8)+('d'*15)+('g'*25)+('x'*4)+('z'*2)
print('original text')
print(str)
c=huffman_coding()
compress_txt=c.Compression(str)
print('compressed text')
print(compress_txt)
decompress_txt=c.decompress(compress_txt)
print('decompressed text')
print(decompress_txt)
print(c.code)
print('original btye',len(str))
print('compress btye',len(compress_txt)/8)



        

        
        


        
