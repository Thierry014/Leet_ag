dic = {'name':{'first':'Thierry', 'last':'Henry'},
       'age':6,
       'gender':'male',
        'gender1':'male',
         'gender2':'2'
        
        
}
# dic = {"key": {"deeper": {"more": {"enough": "value"}}}}



def myprint(d, label = ''):
    
    for k, v in d.items():
        if isinstance(v, dict):
            label += (f'{k}/')
            myprint(v,label)

        else:
            print(f'{label}{k}:{v}')
            label = ''


    
        
myprint(dic)