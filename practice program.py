# 1 craete a list with elements even odd and zero and filter the elements to different list 
'''list=[0,1,2,3,4,5,6,7,8,9,10]'''
'''oddlist=[]
evenlist=[]
zerolist=[]
for i in list:
    if i%2==0 and i!=0:
        evenlist.append(i)
    elif i%2==1:
        oddlist.append(i)
    elif i==0:
        zerolist.append(i)
print(evenlist)
print(oddlist)
print(zerolist)

'''

# 2
'''mylist=[]
limit=int(input('enetr a limit'))
for i in range(limit):
    element=int(input('enter a value'))
    mylist.append(element)
print(mylist)
#mid=limit//2
mylist.insert(limit//2,100)
print(mylist)'''
#3 remove middle part

'''mylist=[]
limit=int(input('enetr a limit'))
for i in range(limit):
    element=int(input('enter a value'))
    mylist.append(element)
print(mylist)
mid=limit//2
mylist.remove(mid)
print(mylist)'''

# 4

a=[1,2,3,4,5,6]
newlist=[]
lim=len(a)
print(len(a))
first=a[0]
print('first:  ',first)
last=a[lim-1]
print('last',last)
mid=a[1:lim-1]
print('mid',mid)
newlist.append(last)
newlist+=mid
newlist.append(first)
print(newlist)
# 5 find the length of a list in python in two ways
'''list=[1,2,3,4,5,6,7,8,9,10]
print(len(list))'''

#6 check if elemnt exists in list

'''print(5 in list)'''

#7 python program to count even and odd numbers in a list
'''evencount=[]
oddcount=[]
for i in list:
    if i%2==0:
        even.count
    else:
        odd.count'''
# 8
'''list=['apple','bannana','mulberry',['cherry',['cashew','litchi',['tomato','chilli','ginger'],'grape'],'lemon'],'mango','orange']
print(list[4])
#mango
print(list[3][1][2][1])
#chilli
print(list[2])
#mulberry
print(list[3][2])
#lemon
print(list[3][1][2])
#['tomato', 'chilli', 'ginger']
print(list[3][:2])'''

#1 python program to interchange first and last elements in a list

#2 different ways to clear a list in python
'''list=[1,2,3,4,5]
list.clear()'''

#3 maximum of two numbers in python

'''a=[1,2,3,3,3,4,6,5,8,19,23]'''
'''print(max(a))'''

#4 minimum of two numbers i python
'''print(min(a))'''

#5 reverse
'''print(a[::-1])'''

#6 check element exist in a list
'''print(2 in a )'''

#7 count
'''print(a.count(3))'''

# 8 print even numbers
'''for i in a:
    if i%2==0:
        print(i)'''
#9 positive and negative numbers in a list
'''list=[1,2,3,4,5,6,-1,-10,-90,7,8,9]'''
'''positivelist=[]
negativelist=[]
for i in list:
    if i>0:
        positivelist.append(i)
    else:
        negativelist.append(i)
print(positivelist)
print(negativelist)'''
#10 remove multiple elements from a list in python list
'''list.remove(2)
print(list)'''

#11 remove empty list from a list
# 12 reverse row
'''list=[[4,1,6],[7,8],[4,10,8]]
print(list[::-1])'''
#13 find uncommon elements in list

#14
'''list=[1,2,3,1,2,3,2,3,87,87,65,87,9,9,67,9]'''

#15
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
for i in range(limit):
    for j in range(i+2):
        print(' ',end='')
    for k in range(limit-i*2):
        print('*',end='')
    print()'''

#16 w
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==0 or j==limit-1 or i==j and i>limit//2 and j>limit//2 or i+j==limit-1 and i>=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        '''

