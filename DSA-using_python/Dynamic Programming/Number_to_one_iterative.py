import sys
def Number_to_one_iterative(num):
    memory=[-1 for ele in range(num+1)]
    memory[1]=0
    i=2
    while i!=num+1:
        less_one,divide_two,divide_three=sys.maxsize,sys.maxsize,sys.maxsize
        less_one=memory[i-1]
        if i%2==0:divide_two=memory[i//2]
        if i%3==0:divide_three=memory[i//3]
        memory[i]=1+min(less_one,divide_two,divide_three)
        i+=1
    return memory[num]

num=int(input('Enter Number'))
print(Number_to_one_iterative(num))