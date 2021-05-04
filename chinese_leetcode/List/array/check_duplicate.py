def check_dup(l1):
    return len(l1) != len(set(l1))

print(check_dup([1,2,3,1]))