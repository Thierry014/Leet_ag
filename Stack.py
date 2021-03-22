def valid(str):
    start = ['(','[','{']
    end = [')',']','}']

    stack = []

    for i in str:
        if i in start:
            stack.append(i)
        else:
            if i in end and stack[-1] == start[end.index(i)]:
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True


print(valid('()[}{}'))