'''tuple1=(1,2,'apple',4,'orange',7,9,'kiwi',30)
print(type(tuple1))
'''
'''tuplea=(1,)
print(type(tuplea))'''

'''tuple2=1,2,4,5,6,7,8,
print(type(tuple2)
print(a[2])
print(a[-2])
print(len(tuple2))
'''
'''print(tuple1+tuple2)'''
'''tuple3=(tuple1,tuple2)
print(tuple3)
print(len(tuple3))
print(2 in tuple2)
print(10 in tuple2)
print(7 in tuple3[0])'''

'''tuple4=(1,2,3,4,5,6,7,8,9,10)
for i in tuple4:
    if i%2==0:
        print(i)

tup1=('python',)*3
print(tup1)'''

#WHY TUPLE IS IMMUTABLE

#not reassign
'''tuple1=(0,1,2,3)
tuple1[0]=4
print(tuple1)
TypeError: 'tuple' object does not support item assignment
'''
#not possible to delete
'''tuple3=(0,1)
del tuple3[0]
print(tuple3)
TypeError: 'tuple' object doesn't support item deletion'''

#cannot append
'''tuple1=(1,1,2,3,4)
tuple.append(5)
AttributeError: type object 'tuple' has no attribute 'append'''

#cannot remove
'''tup=('apple','banana','cherry')
tup.remove('apple')
print(tup)'''
#AttributeError: 'tuple' object has no attribute 'remove'

'''tup=('apple','banana','cherry')
print(type(tup))'''
'''list1=list(tup)
print(type(list1))
'''
'''a=('apple','banana','cherry')
y=list(a)
y.append('orange')
a=tuple(y)
print(a)

list1=list(tup)
print(type(list1))'''

'''tup=('apple','banana','cherry')
for i in range(3):
    print(tup[i])'''


'''tup=('apple','banana','cherry')
i=0
while i<len(tup):
    print(tup[i])
    i+=1'''

'''tup=('kiwi','orange','mango')
i=0
while i<len(tup):
    print(tup[i])
    i+=1

for i in range(3):
    print(tup[i])'''


#packing
'''A='PYTHON IS SIMPLE'
print(tuple(A))'''
'''Tuple1=[1,2,3,4]
print(Tuple1)
a,b,c,d=Tuple1
print(a,b,c,d)'''

#count
'''tup=(1,3,7,8,5,7,5,4,6,8,5)
x=tup.count(5)
print(x)
'''
#sum, len,max,min,index 
'''sum1=sum(tup)
print(sum1)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(5))
'''

#ZIPPING

'''first_names=('simon','Sarah','Mehadi','Fatime')
last_names=('Sinek','Smith','Lotfinejad','Lopes')
ages=(49,55,39,33)
zipped=zip(first_names,last_names,ages)
print(list(zipped))'''
      

'''a=[1,]
b=[10,11,23,45]
a.extend(b)
print(a)'''


