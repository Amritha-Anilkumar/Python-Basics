#SWAPPING 

'''A=int(input('enter a value'))
B=int(input('enter a value'))'''
'''Temp=A
A=B
B=Temp'''
'''A,B=B,A
print(A,B)'''

#FIBONOCCI SERIES
'''a=int(input('enter a value'))
b=int(input('enter a value'))
sum=0
i=0
while i<=7:
    print(a)
    sum=a+b
    a=b
    b=sum
    i=i+1'''


#sum of fibonocci series
'''a=int(input('enter a value'))
b=int(input('ener a value'))
sum=0
i=0
total=0
while i<=7:
    print(a)
    total=total+a
    sum=a+b
    a=b
    b=sum
    i=i+1
print('total=',total)

'''
def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 +sum_of_digits(n//10)
number=1234
print('sum of digits:',sum_of_digits(number))
