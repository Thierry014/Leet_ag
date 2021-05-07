def long_prefix(l1):
    # l1 = ['flower','foden','foul']
    res = ''
    l1 = [list(x) for x in l1]
    l1_tup = tuple(l1)
    list_zip = list(zip(*l1_tup))

    for i, tup in enumerate(list_zip):
        print(tup)
        if len(set(tup))==1:
            res += tup[0]
    
    return res
            



print(long_prefix(['flower','floden','floul']))