#  must use recusive method to handle those type of problem 
dic = {'name':{'first':'Thierry', 'last':'Henry'},
       'age':6,
       'gender':'male',
        'gender1':'male',
         'gender2':'2'
        
        
}

def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))

myprint(dic)