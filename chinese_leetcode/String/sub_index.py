def substr(s,t):
    if len(t) == 0:
        return 0 
    return s.find(t[0])

print(substr('hello','ll'))
print(substr('aaa','bba'))
print(substr('aaa',''))