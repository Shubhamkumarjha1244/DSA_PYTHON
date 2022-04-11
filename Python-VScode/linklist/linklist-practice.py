def letter(num):
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
        return ' '
def letterCombinations(digits: str):
        if len(digits)==0:
            output=[]
            output.append('')
            return output
        ones=(int(digits))%10
        alpha=letter(ones)
        small_num=(int(digits))//10
        
        output=[]
        for i in alpha:
            for j in letterCombinations(str(small_num)):
                combi=i+j
                output.append(combi)
        return output
                

letterCombinations('23')