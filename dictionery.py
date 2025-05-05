'''dict1={'name':'amritha','age':22,'place':'kozhikode'}
print(dict1)'''

#duplication not allowed 
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
print(dict1)'''

#length 
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
print(len(dict1))'''

#dictionary item 
'''dict2={'brand':'ford','electric':'false','year':1964,'colors':['red','white','blue']}
print(dict2)'''

#type
'''dict2={'brand':'ford','electric':'false','year':1964,'colors':['red','white','blue']}
print(type(dict2))'''

'''dict1=dict(name='amritha',age=22,place='kozhikode')
print(dict1)'''

#get a value
'''dict1=dict(nam
print(dict1['place'])'''
'''print(dict1.get('place'))
ans=kozhikode'''

#keys 
'''x=dict1.keys()
print(x)
ans=dict_keys(['name', 'age', 'place'])'''

#values
'''x=dict1.values()
print(x)
ans=dict_values(['amritha', 22, 'kozhikode'])'''

#items 
'''dict1=dict(name='amritha',age=22,place='kozhikode')
x=dict1.items()
print(x)'''

#add a value 
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
dict1['email']='amritha@gmail.com'
print(dict1)'''

#exist
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
print('name' in dict1)'''

#change value 
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
dict1['place']='kozhikode'
print(dict1)
'''

#update 
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
x=dict1.update({'age':23,'lname':'p'})
print(dict1)'''

#pop
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
x=dict1.pop('name')
print(dict1)'''

#popitem(remove lats item)
'''dict1={'name':'amritha','age':22,'place':'kozhikode','place':'calicut'}
x=dict1.popitem()
print(dict1)'''

#delete
'''dict1={'name':'amritha','age':22,'place':'kozhikode'}
del dict1['name']
print(dict1)'''

'''dict1={'name':'amritha','age':22,'place':'kozhikode'}
del dict1
print(dict1)
'''

#clear 
'''dict1={'name':'amritha','age':22,'place':'kozhikode'}
dict1.clear()
print(dict1)'''

#exercise
'''sample={'class':{'student':{'name':'mike','marks':{'physics':70,'history':80}}}}
print(sample['class']['student']['marks']['physics'])
#ans-70
print(sample['class']['student']['name'])
#ans-mike
print(sample['class']['student']['marks']['history'])
#ans-80'''

#
'''keys=['ten','twenty','thirty']
values=[10,20,30]
dict1={}

for j in range(3):
    dict1[keys[j]]=values[j]
print(dict1)'''

#
'''dict1={'ten': 10, 'twenty': 20, 'thirty': 30}
dict2={'thirty':30,'fourty':40,'fifty':50}
x=dict1.update(dict2)
print(dict1)
#ans-{'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50}'''



#create a 1**2 dictionery 
"""limit=int(input('enter a value'))
dict1={}
for i in range(1,limit+1):
    dict1[i]=i**2
print(dict1)
#ans-{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}"""

#
'''string1='python is an interpreted programming language'
dict1={}
words=string1.split()
print(words)
for i in words:
    if i[0] not in dict1:
        dict1[i[0]]=[]
        dict1[i[0]].append(i)
    else:
        dict1[i[0]].append(i)

print(dict1)'''

#1214
'''n=input('enter a value')
nn1={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
pn1={1:'once',2:'tens',3:'hundreds',4:'thousands',5:'tenthousand',6:'lakhs'}
value=''
print(len(n))
l=len(n)
for i in n:
    value+=nn1[i]+' '+pn1[l]+' '+' '
    l=l-1
print(value)
#ans-one thousands  two hundreds  one tens  four once'''

#create a dictionery 
limit=int(input('enter a value'))
i = 0
while i < limit:
    value = int(input('enter a value'))
    i += 1








    
 

