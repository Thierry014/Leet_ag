
# TODO  (Find the largest key based on the key value) => return key (with max value) => in dict 

stats = {'a':1000, 'b':3000, 'c': 100}
max_key = max(stats, key=lambda k: stats[k])
max_k = max(stats, key=stats.get)



test = {'a':1000, 'b':3000, 'c': 100} 
k = test.get
# print(k)


#! k = get method => container all the keys 


# TODO  (Find the largest value based on the key name) => return a sorted list  =>  in list
dic = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]


newlist = sorted(dic, key=lambda k: k['price'],reverse=True) 
print(newlist)


dic_num = {-20: 20, -5: 5, 10: 10, 15: 15}

print(sorted(dic_num, key = lambda k: dic_num[k]))