def letter_combination(num):
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

def phone_combination(num):
    if num==0:
        output=[]
        output.append('')
        return output
    
    digit=num%10
    smallernumber=num//10
    smallercombination=phone_combination(smallernumber)
    digitcombination=letter_combination(digit)
    output=[]
    for alp in digitcombination:
        for ele in smallercombination:
            word=alp+ele
            output.append(word)
    return output


combination=23
print(phone_combination(combination))