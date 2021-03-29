import functools
def numToMobile(digits):
    maps = {
        '2':'abc',
        '3':'def',
        '4':'hig',
        '5':'klm',
        '6':'opq',
        '7':'rst',
        '8':'uvw',
        '9':'xyz',
    }

    return functools.reduce(lambda acc,digit : [ x+y for x in acc for y in maps[digit]],digits, [''])

print(numToMobile('2355'))
