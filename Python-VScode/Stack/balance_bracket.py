
# #mine solution

# def validated_bracket(arr):
#     stack=[]
#     for ele in arr:
#         if ele == '(' or ele == '{' or ele == '[' :
#             stack.append(ele)
#             continue
#         elif len(stack)==0 and (ele == '}' or ele == ']' or ele == ')'):
#             stack.append(ele)
#             continue
#         elif ele == '}':
#            if stack[len(stack)-1]== '{':
#                stack.pop()
#                continue
#         elif ele == ']':
#            if stack[len(stack)-1]== '[':
#                stack.pop()
#                continue
#         elif ele == ')':
#            if stack[len(stack)-1]== '(':
#                stack.pop()
#                continue
#     return  len(stack)==0

# stri='[[[]]]'
# print(validated_bracket(stri))




def validate(stri):
    stack=[]
    for ele in stri:
        if ele in '({[':
            stack.append(ele)
        elif ele ==']':
            if(not stack or stack[-1] !='['):
                return False
            stack.pop()
        elif ele ==')':
            if (not stack or stack[-1] !='('):
                return False
            stack.pop()
        elif ele =='}':
            if (not stack or stack[-1] !='{'):
                return False
            stack.pop()
    return  len(stack)==0

            
stri=input()
print(validate(stri))