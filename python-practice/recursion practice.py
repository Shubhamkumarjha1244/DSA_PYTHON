# # import queue


# # class recursion:
# #     def __init__(self):
# #         self.output=[]
        

# #     def total_subset(self,arr):
# #         if len(arr)==0:
# #             return ['']
# #         first_ele=str(arr[0])
# #         second_subset=self.total_subset(arr[1:])
# #         ans=[]
# #         for ele in second_subset:
# #             ans.append(first_ele+ele)
# #             ans.append(ele)
# #         return ans
        
# #     def total_combination(self,pos,arr,target,ans):
# #         if target==0 and pos<len(arr):
# #             self.output.append(ans)
# #             return
# #         if pos>=len(arr) or target<0:
# #             return 
        
# #         self.total_combination(pos,arr,target-arr[pos],ans+[arr[pos]])
# #         self.total_combination(pos+1,arr,target-arr[pos+1],ans+[arr[pos+1]])



        
# #     def total_permutation(self,arr):
# #         if len(arr)==0:
# #             return [""]
# #         ans=[]
# #         for i in range(len(arr)):
# #             per=str(arr[i])
# #             rest=arr[:i]+arr[i+1:]
# #             for ele in self.total_permutation(rest):
# #                 ans.append(per+ele)
# #         return ans


            

# #     def unique_subset(arr):
# #         pass
# #     def unique_combination(arr):
# #         pass

# # rec=recursion()
# # print(rec.total_subset([1,2,3,3]))
# # rec.total_combination(0,[1,2,3,3,4],8,[])
# # print(rec.output)
# # print(rec.total_permutation([1,2,3]))


# # qu=queue.Queue()

# # qu.put(qu.get)

# import queue
# def deckRevealedIncreasing(deck):
#         sorted_deck=sorted(deck)
#         qu=queue.Queue()
#         qu.
#         for i in range(0,len(deck)):qu.put(i)
#         for i in range(0,len(deck)):
            
#             deck[qu.get()]=sorted_deck[i]
#             qu.put(qu.get())
#             print(deck)
#         print('end')
#         return deck

# deck=[17,13,11,2,3,5,7]
# print(deckRevealedIncreasing(deck))


# import heapq
# def kMaxSumCombination(a, b, n, k):
#      arr=[]
# 	 for ele_a in a:for ele_b in b:arr.append(ele_a+ele_b)
#     heapq._heapify_max(arr)
#     ans=[]
#     for i in range(k):
#         ans.append(heapq._headpop_max(arr))
#     return ans