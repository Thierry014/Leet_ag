str = 'heloo 123'
str = str.split(' ')
print(str)
print([int(x) for x in str if x.isdigit()])