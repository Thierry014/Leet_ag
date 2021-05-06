def rev_num(num):
    if num == 0:
        return 0
    
    sign = 1
    res = ''

    if num<0:
        num = num*-1
        sign = -1

    while num:
        res += str(num%10)
        num //=10
    
    return int(res)*sign


print(rev_num(-120))



