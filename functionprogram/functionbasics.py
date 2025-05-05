#area calculation 
'''def area(r):
    a=3.14*r*r
    return a


radius=int(input('enter a value'))
print(area(radius))'''

#even or odd
'''def even(n):
    if n%2==0:
        return 'the given number is even'
    else:
        return 'the given number is odd'
n=int(input('enter a value'))
print(even(n))'''
#sequences program 

#add two number 
'''def num(a,b):
    c=a+b
    return c
print(num(10,15))'''

#area of a square 
'''def area(a):
    b=a**2
    return b
a=int(input('enter a value'))
print(area(a))'''

#rectangle
'''def rectangle(l,b):
    a=l*b
    return a
print(rectangle(10,5))'''

#simple intrest 
'''def simpleintrest(p,n,r):
    a=p*n*r/100
    return a 
print(simpleintrest(1000,4,2))'''

#condtion statement 

#which number is bigger 
'''def num(a,b):
    if a<b:
        return 'b is bigger'
    else:
        return 'a is bigger'
print(num(2,4))'''

#check the given number is multiple of 5
'''def num(a):
    if a%5==0:
        return 'the given number is multiple of 5'
    else:
        return 'the given number is not a multiple of 5'
a=int(input('enter a value'))
print(num(a))
'''

#check the person is eligible for voting 
'''def age(n):
    if n>18:
        return 'the person is eligible for voting'
    else:
        return 'the person is not eligible for voting'
n=int(input('enter a value'))
print(age(n))'''

#positive,negative,zero
'''def num(n):
    if n<0:
        return 'the number is negative'
    elif n>0:
        return 'the number is positive'
    else:
        return 'the number is zero'
n=int(input('enter a value'))
print(num(n))'''

#FOORLOOP

'''def a(limit):
    sum=0
    for i in range(limit):
        num=int(input('enter a value'))
        sum=sum+num
    return sum

limit=int(input('enter a limit'))
print(a(limit))'''


'''def  multi(limit,multi):
    for i in range(1,limit+1):
        product=i*multi
        print(i,'*',multi,'=',product)
limit=int(input('enter a limit'))
m=5
print(multi(limit,m))'''

#whileloop
'''def count(limit):
    count=0
    while count<limit:
        print(count)
        count+=1
limit=int(input('enter a value'))
count(limit)'''

#list
'''def even(numbers):
    even_numbers=[]
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
num=[1,2,3,4,5,6,7,8,9,10]
print(even(num))'''

#
'''def add_numbers(num1):
    sum=num1+num2
    print('sum:',sum)
add_numbers(5,4)
add_numbers() takes 1 positional argument but 2 were given'''

#tuple
'''def fruites(z):
    y=list(z)
    y.append('orange')
    a=tuple(y)
    print(y)
z=('apple','banana','cherry')
fruites(z)'''











    
