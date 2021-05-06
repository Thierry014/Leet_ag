def acco(str):
    str=str.replace(' ','').lower()

    for i, char in enumerate(str):
        if not (char.isalpha() or char.isdigit()):
            str = str.replace(char,'')
    
    lens = len(str)

    if lens<=1:
        return str
    elif lens%2 == 0:
        return str[:lens//2] == str[lens//2:][::-1]
    else:
        return str[:lens//2] == str[lens//2+1:][::-1]
        


print(acco('A man, a plan, a canal: Panama'))
print(acco('abc:676,,,cba'))