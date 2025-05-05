#creating a function 
'''def greet():
    print('Hello World!')
greet()'''

#calling a function 
'''def name():
    print('AMRITHA')
name()
print('outside function')'''

#Arguments in function 
'''def my_function(name):
    print(name+' is my name')
my_function('Amritha')
my_function('sreerag')'''

'''def add_num(a,b):
    c=a+b
    print(c)

add_num(12,8)
add_num(10,5)
add_num(2,18)'''

'''def add_3num(a,b,c):
    d=a+b+c
    print(d)
add_3num(5,15,20)'''

#defalut parameter value
'''def add_numbers(num1=200,num2=100):
    sum=num1+num2
    print('sum:',sum)
add_numbers(5)
add_numbers(5,10)
add_numbers()'''

'''def add_num(a,b):
    c=a+b
    return c
print(add_num(12,8))
print(add_num(10,8))
sum=add_num(10,5)
print(sum)'''

'''def function_num(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print(c,d,e,f)
function_num(10,5)'''


'''def function_num(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return (c,d,e,f)
    #below line does not execute because after return statement the controll will moves to the place were the function is called .
    print('hello world')
print(function_num(10,5))'''

'''def function_num(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return {'addition':c,'substractin':d,'multiplication':e,'division':f}
print(function_num(10,5))'''
#LOWER 
'''def name(b):
    a=b.lower()
    return a    
print(name('HELlow 123 WoRLd 45'))
'''
#UPPER 
'''def name(b):
    a=b.upper()
    return a    
print(name('HELlow WoRLd '))
'''
'''def name(a):
    b=a.isdigit()
    return b 
print(name('HELlow 123 WoRLd 45'))'''

#Arbitary Arguments
'''def find_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num
    print('sum=',result)
find_sum(1,2,3)
find_sum(2,3,4,5,6,7)'''

#Key word argument 
'''def full_name(first_name,last_name):
    print('first_name:',first_name)
    print('last_name:',last_name)
    name=first_name+ ' '+last_name
    print(name)
full_name(last_name='MARIA',first_name='ANN')'''

#passing list as a argument 
'''def my_function(food):
    for i in food:
        print(i)
fruites=['apple','orange','banana']
my_function(fruites)'''

#lambda
'''sum=lambda arg1,arg2:arg1+arg2
print('value of total:',sum(10,20))
print('value of total:',sum(30,20))'''

# check even 
'''even=lambda value:value%2==0
print(even(4))'''

#square
'''s=lambda value:value**2
limit=int(input('enter a value'))
print(s(limit))'''

#scope of variables 
'''def sum(arg1,arg2):
    total=arg1+arg2
    print('inside the function local total:',total)
    return total 
sum(10,20)
print(total)#name 'total' is not defined'''

'''total=20
def sum(arg1,arg2):
    total=arg1+arg2
    print('inside the function local total:',total)
    return total 
sum(10,20)
print(total)'''

#RECRUSIVE FUNCTION 
'''def recursion(n):
    if n<=1:
        return n
    else:
        return n+recursion(n-1)
s=recursion(5)
print(s)'''

#
'''def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(5))'''

#KEY WORD ARGUMENTS(*kwargs)
'''def students(**stud):
    print('name:'+stud['name']+' ','age','=',stud['age'])
students(name='Ann',age=22)'''

#1 to 10 number's sum 
'''def sum(n):
    if n<=1:
        return 1
    else:
        return n+sum(n-1)
s=sum(10)
print(s)'''

# 1 to number's multiplication 
'''def sum(n):
    if n<=1:
        return 1
    else:
        return n*sum(n-1)
s=sum(10)
print(s)'''

#contact book 
'''contactbook={}
while True:
    print("\nContact Book Menu")
    print('1. Add contact')
    print('2. View contact')
    print('3. Search contact')
    print('4. Delete contact')
    print('5. Exit contact')
    choice=input('enter your choice: ')
    if choice=='1':
        name=input('enter your name')
        phone=input('enter your phone number')
        if name in contactbook:
            print(f"{name} already in the contact book")
        else:
            contactbook[name]=phone
            print(f"contact name add succesfully")
    elif choice=='2':
        if not contactbook:
            print('contact book is empty')
        else:
             print('n/contacts:')
             for name, phone in contactbook.items():
                 print(f"{name}= {phone}")
    elif choice=='3':
        name=input('enter the name to search')
        if name in contactbook:
            print(f"{name}={contactbook[name]}")
        else:
            print(f"{name} not found in contactbook")
    elif choice=='4':
        name=input('enter name to delete')
        if name in contactbook:
            del contactbook[name]
            print(f"{name} deleted succesfully")
        else:
            print(f"{name} not found in the contactbook")
    elif choice=='5':
        print('exiting contact book. Goodbye')
        break
    else:
        print('invalid contact please try again')'''



'''while True:
     print("\nContact Book Menu")
     print('1. UPPERCASE')
     print('2. LOWERCASE')
     print('2. SPLIT')
     choice=input('enter your choice: ')
     if choice=='1':
          name=input('enter your string')
          print(name.upper())
     elif choice=='2':
        name=input('enter your string')
        print(name.lower())
     elif choice=='3':
         name=input('enter your string')
         print(name.split(','))
     else:
         print('not found')'''

#MAP 
'''def calculatesqure(n):
    return n*n
numbers=(1,2,3,4)
result=map(calculatesqure,numbers)
print(list(result))'''

        
#lambda function to map
'''numbers=(1,2,3,4)
result=map(lambda x:x*x,numbers)
print(tuple(result))'''

'''num1=[1,2,3,4]
num2=[5,6,7,8]
result=map(lambda n1,n2:n1+n2,num1,num2)   
print(list(result)) '''      

#FILTER 
'''letters=['a','b','d','e','i','j','o']
def filter_vowels(letter):
    vowels=['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False
filter_vowels=filter(filter_vowels,letters)
print(tuple(filter_vowels))'''

#using lambda function in filter 
'''numbers=[1,2,3,4,5,6,7]
even_numbers=filter(lambda x:(x%2==0),numbers)
print(tuple(even_numbers))'''


'''numbers=[1,2,5,3,4,10,15,20,65,33,45,14,24,90]
multi_numbers=filter(lambda x:(x%5==0),numbers)
print(tuple(multi_numbers))'''

#reduce
'''from functools import reduce
def do_sum(x1,x2):
    return x1+x2
print(reduce(do_sum,[1,2,3,4]))'''

#doc attribute (read the comment)
'''def squre(n):
    'takes in a number n ,return the squre of n'
    return n*2
print(squre.__doc__)'''
'''
def add_numbers(*args):
    total=0
    for num in args:
        total+=num
        return total
print("sum:",add_numbers(10,20))
print("sump",add_numbers(5,15,25,35))'''

'''def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n=n//10
    return total
print("sum of digits:", sum_of_digits(12345))
'''

def sum(numbers):
    total=0
    for num in numbers:
        total+=num 
    return total
my_list=[10,20,30,40]
print('sum of list elements:',sum(my_list))




                  
    
    

    
    
    



















