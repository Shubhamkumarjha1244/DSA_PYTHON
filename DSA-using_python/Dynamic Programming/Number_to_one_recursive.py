import sys
def Number_to_one(num,memory):
    if num==1:return 0
    if memory[num-1]!=-1:
        num_reduce_one=memory[num-1]
    else:
        num_reduce_one=Number_to_one(num-1,memory)
        memory[num-1]=num_reduce_one
    num_divideThree=sys.maxsize
    if num%3==0:
        if memory[num//3]!=-1:
            num_divideThree=memory[num//3]
        else:
            num_divideThree=Number_to_one(num//3,memory)
            memory[num//3]=num_divideThree
    num_divideTwo=sys.maxsize
    if num%2==0:
        if memory[num//2]!=-1:
            num_divideTwo=memory[num//2]
        else:
            num_divideTwo=Number_to_one(num//2,memory)
            memory[num//2]=num_divideTwo
    return 1+min(num_divideTwo,num_divideThree,num_reduce_one)

    






num=int(input('Enter Number'))
memory=[-1 for ele in range(1,num+1)]
print(Number_to_one(num,memory))