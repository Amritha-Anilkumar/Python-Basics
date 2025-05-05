#set 
'''a={1,2,3,4,5,6,7,'kiwi',8,9,10,11,12,13,'apple','orange','mango',5,6}
print(a)
print(type(a))
print(len(a))'''
'''
numlist=[1,2,3,4,5,6,7,8,9,1,2,3]
no_dup=[]
set_num=set(numlist)
for i in set_num:
no_dup.append(i)
print(no_dup)
# numlist.append(10)
# print(numlist)'''

#0=false
#1=true

'''A={0,True,1,False,'apple',2,0,'orange'}
print(len(A))
print(A)'''

'''thisset={'apple','apple','banana','cherry'}
for x in thisset:
    print(x)
print('apple' in thisset)'''

'''a={'apple','banana','cherry'}
a.add('orange')
print(a)
b=['kiwi','pappaya']
a.update(b)
print(a)
fruits={'apple','banana','cherry'}
fruits.remove('banana')
print(fruits)
fruits=['apple','banana','cherry']
x=fruits.pop()
print(x)'''

#pop-randlomly remove 
'''fruits={'apple','banana','cherry'}
x=fruits.pop()
print(x)'''

'''a=set()
print(type(a))'''

'''a={}
print(type(a))'''

'''fruits={'apple','banana','cherry'}
# del fruits
# print(fruits)
fruits.clear()
print(fruits)'''

#union
'''set1={'a','b','c'}
set2={1,2,3}
set3=set1.union(set2)
print(set3)'''

'''set1={'a','b','c','d'}
set2={1,2,3,'d'}
set3=set1.union(set2)
print(set3)'''

#INTERSECTION 
'''set1={'a','b','c','d'}
set2={1,2,3,'d'}
SET4=set1.intersection(set2)
print(SET4)'''

#INTERSECTION UPDATE 
'''set1={'a','b','c','d'}
set2={1,2,3,'d'}
set1.intersection_update(set2)
print(set1)'''

#DIFFERENCE
'''X={'apple','banana','orange'}
Y={'microsoft','google','apple'}
Z=X.difference(Y)
print(Z)
#{'banana', 'orange'}'''

#DIFERRENCE UPDATE 
'''X={'apple','banana','orange'}
Y={'microsoft','google','apple'}
X.difference_update(Y)
print(X)
#{'banana', 'orange'}'''

#SYMETRIC DIFFERENCE 
X={'apple','banana','orange'}
Y={'microsoft','google','apple'}
X.symmetric_difference_update(Y)
print(X)
#{'microsoft', 'orange', 'banana', 'google'}

#ADD A LIST OF ELEMENT TO SET 
'''a={1,2,3,4,5,6}
b=[7,8,9,10,11,12,13]
a.update(b)
print(a)
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}'''

#RETURN A NEW SET OF IDENTICAL ITEM FROM TWO SET 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26}
c=a.intersection(b)
print(c)
#{1, 2, 3}'''

#GET ONLY UNIQUE ITEM FROM TWO SET 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26}
c=a.union(b)
print(c)
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 26}'''

#UPDATE THE FIRST SET WITH ITEMS THAT DONT EXIST IN SECOND SET 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26}
a.difference_update(b)
print(a)
#{4, 5, 6, 7, 8}'''

#REMOVE ITEMS FROM SET AT ONCE 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26}
a.difference_update(b)
print(a)
#{4, 5, 6, 7, 8}'''

#RETURN A SET OF ELEMENTS IN SET A OR B,BUT NOT BOTH 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26,8,34,5}
a.symmetric_difference_update(b)
print(a)
#{34, 4, 6, 7, 9, 13, 14, 26}'''

#CHECK IF TWO SET HAVE ANY ELEMENTS IN COMMON.IF YES DISPLAY COMMON ELEMENTS 
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26,8,34,5}
c={11,12}
if a.isdisjoint(b):
    print('there is no common elements')
else:
    print(a.intersection(b),'common element')
#{1, 2, 3, 5, 8} common element'''

#UPDATE SET 1 BY ADDING ITEMS FROM SET 2,EXCEPT COMMON ITEM
'''a={1,2,3,4,5,6,7,8}
b={9,1,2,3,13,14,26,8,34,5}
a.symmetric_difference_update(b)
print(a)
{34, 4, 6, 7, 9, 13, 14, 26}'''
'''a={'apple','banana','cherry'}
a.add('orange')
print(a)
b=['kiwi','pappaya']
a.update(b)
print(a)'''




