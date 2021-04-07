def findword(para, word):
    word = word.lower()
    para = para.replace(' ','').lower()
    row_list = para.split('\n')
    res = []

    # check in row 
    for i, v in enumerate(row_list):
        if word in v:
            index = v.find(word)
            print([i+1,index+1,i+1,index+len(word)])
            res = [i+1,index+1,i+1,index+len(word)]
    
    #check in col
    col_list = list(zip(*row_list))
    col_list = [('').join(x) for x in col_list]

    for i,v in enumerate(col_list):
        if word in v:
           index = v.find(word)
           print([index+1,i+1,index+len(word),i+1])
           res = [index+1,i+1,index+len(word),i+1]



    return res


para1 = """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!"""

para2 = """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?"""

# findword(para1,'noir') => [4, 16, 7, 16]
# findword(para2,'ten') => [2, 14, 2, 16]
findword(para1,'noir')
findword(para2,'ten')

