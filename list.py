'''list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=["a","b","c","d"]'''
'''print(list1)
print(list2)
print(list3)

print(list1[1])
print(list2[3])'''
#replace
'''list1[2]='AMRITHA'
print(list1)
['physics', 'chemistry', 'AMRITHA', 2000]'''

#delete
'''del list1[2]
print(list1)
['physics', 'chemistry', 2000]'''

'''del list1
print(list1)'''

#Clear
'''list1.clear()
print(list1)
[]'''

#length
'''print(len(list1))
4'''
#concatenation
'''print(list1+list2)

['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]'''

#Repetition
'''a=[1,2]
print(a*3)
[1, 2, 1, 2, 1, 2]
'''
#Membership
'''a=[1,2]
print(2 in a)
ans-True'''

#LOOPING
list1=['physics','chemistry',1997,2000,4500,9000]
#literation through a list 
'''for i in list1:
    print(i)'''
#NEGATIVE INDEXING 
'''print(list1[-1])
print(list1[-2])'''

#SLICING 

'''print(list1[::-1])
[9000, 4500, 2000, 1997, 'chemistry', 'physics']'''

#listName[Start:Stop:step]
numlist=[1,2,3,4,5,6,7,8,9]
'''print(numlist[5])
print(numlist[2:7:])
print(numlist[2:7:2])
print(numlist[:7:])
print(numlist[::2])
print(numlist[4::])
print(numlist[4::-1])
print(numlist[7:1:-1])      
print(numlist[::-1])
print(numlist[2:7:2])
6'''
'''[3, 4, 5, 6, 7]
[3, 5, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 3, 5, 7, 9]
[5, 6, 7, 8, 9]
[5, 4, 3, 2, 1]
[8, 7, 6, 5, 4, 3]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
'''


#craete a list and insert values randomly find only the even numbers

'''list=[22,31,43,77,88,92,80,30,31,67]
for i in list:
    if i%2==0:
        print(i)'''
#NEGATIVE
'''list=[1,-5,8,-10,-27,8,9,10]
for i in list:
    if i<0:
        print(i)'''

#MULTIPLICATION 7
'''list=[7,70,55,14,21,10]
for i in list:
    if i%7==0:
        print(i)'''

#MULTIPLICATION OF 7 AND 3
'''list=[7,3,21,15,77,30,18,12]
for i in list:
    if i%7==0 or i%3==0:
        print(i)
  '''  
#append
'''numlist=[1,2,3,4,5,6,7,8,9]
numlist.append(10)
print(numlist)'''

'''list=[1,2,22,4,55,7,10,15,9,18]
oddlist=[]
evenlist=[]
for i in list:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(evenlist)
print(oddlist)'''


#extend(compine 2 list)
'''list5=[1,]
list8=[10,11,23,45]
print(list5.extend(list8))'''

#COUNT (how many times obj occurs in list)

'''list=[123,'xyz','wxy','abc',123]
print(list.count(123))
2

'''
#MIN AND MAX 
'''A=[1,3,4,56,79,33]
print(max(A))
print(min(A))
79
1
'''

#INSERT
'''list=['apple','banana','cherry']
list.insert(2,'watermelon')
print(list)
['apple', 'banana', 'watermelon', 'cherry']

'''

#REMOVE
'''list=['apple','banana','cherry']
list.remove('apple')
print(list)'''

#POP
'''list=['apple','banana','apple','cherry']
list.pop(1)
print(list)

list=['apple','banana','cherry']
list.pop(0)
print(list)

list=['apple','banana','cherry']
list.pop(2)
print(list)
'''

list=['apple','bannana','mulberry',['cherry',['cashew','litchi',['tomato','chilli','ginger'],'grape'],'lemon'],'mango','orange']

'''print(len(list))
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])'''

'''print(list[3][1][0])

print(list[3][1][2][1])'''
'''print(list[3][0])
#cherry
print(list[3][1][0])
#cashew
print(list[3][1][1])
#litchi
print(list[3][1][2])
#['tomato', 'chilli', 'ginger']
print(list[3][1][2][0])
#tomato
print(list[3][1][2][1])
#chilli
print(list[3][1][2][2])
#ginger
print(list[3][1][3])
#grape
print(list[3][2])
#lemon'''

'''numlist=[1,2,3,4,5,6,7,8,9,1,2,3]
no_dup=[]
set_num=set(numlist)
for i in set_num:
    no_dup.append(i)
print(no_dup)
# numlist.append(10)
# print(numlist)'''

'''text="hello world, hi hello"
count=text.count("hello")
print(count)
'''
a="Hello World"
upper_count=0
lower_count=0
for char in a:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
print("upper letters:", upper_count)
print("lower letters:",lower_count)


 
 