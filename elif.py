
#
'''a=int(input('enter a value'))
b=int(input('enter a value'))
if b>a:
    print('b is grater than a')
elif a==b:
    print('a and b are equal')
else:
    print('a is grater than b')'''

#unit consumed
'''UC=int(input('enter the Unit Consumed'))
if UC<=100:
    print('charges:',0.5*UC)
elif UC>100 and UC<200:
    print('charges:',50+1*(UC-100))
elif UC<200 and UC>300:
    print('charges:',150+1.50*(UC-200))
else:
    print('charges:',300+2*(UC-300))
'''

#POSITIVE, NEGATIVE OR ZERO
'''a=int(input('enter a value'))
if a<0:
    print('the number is negative')
elif a>0:
    print('the number is positive')
else:
    print('the number is zero')'''


#NESTEDIF
x=int(input('enter a value'))
if x>10:
    print('above ten')
    if x>20:
        print('and also above 20')
    else:
        print('but not above 20')
        print('but not above 20')
else:
    print('less than 10')
