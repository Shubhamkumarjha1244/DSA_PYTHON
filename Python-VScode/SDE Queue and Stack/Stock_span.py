class StockSpanner:

    def __init__(self):
        self.__data=[]
        

    def next(self, price: int) -> int:
        count=1
        while len(self.__data)!=0 and self.__data[-1][0]<=price:
            count=count+self.__data.pop()[1]
        self.__data.append([price,count])
        print(count)
        return

q=StockSpanner()
q.next(100)
q.next(80)
q.next(60)
q.next(70)
q.next(60)
q.next(75)
q.next(85)
