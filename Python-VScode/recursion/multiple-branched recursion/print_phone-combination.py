def combi(num):
    if num==2:
        return 'abc'
    if num==3:
        return 'def' 
    if num==4:
        return 'ghi'
    if num==5:
        return 'jkl'
    if num==6:
        return 'mno'
    if num==7:
        return 'pqrs' 
    if num==8:
        return 'tuv'
    if num==9:
        return 'wxyz'
    return ''      

def print_phone_combination(num,output):

    if num==0:
        print(output)
        return 

    last_digit=num%10
    smaller_num=num//10
    last_digit_combination=combi(last_digit)
    for i in last_digit_combination:
        newoutput=i+output
        print_phone_combination(smaller_num,newoutput)


combination=34
print_phone_combination(combination,'')

