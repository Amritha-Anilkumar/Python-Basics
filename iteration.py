#iter 
'''num=[1,2,3,4]
obj=iter(num)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))'''
 
#modules
#1.math module
#ciel and floor

'''import math
num1=5
num2=6
division=num1/num2
print(division)
print(math.ceil(division))
print(math.floor(division))'''

#sqrt
'''import math 
num=256
print(math.sqrt(num))'''

#pow
'''import math 
num=int(input('enter the value'))
#square
print(math.pow(num,2))
#cube
print(math.pow(num,3))'''

#pie 
'''from math import pi
print(pi)'''

#example of pie  
'''from math import pi
radious=float(input('enter the radious'))
area=pi*radious*radious
print('area of circle:',area)
perimeter=2*pi*radious
print('peremeter of circle:',perimeter)'''

#factorial 
'''import math 
num=int(input('enter the value'))
print(math.factorial(num))
                    #or
from math import factorial 
num=int(input('enter the value'))
print(factorial(num))'''

#logarithm
'''import math 
num=int(input('enter the number'))
print(math.log(num))'''

#cheking files in math module
'''import math 
print(dir(math))#dir=directory '''

#degree radiant 
'''from math import* # *helps to import all the math files in the program 
angle=10
degree_angle=radians(angle)
degree_angle=degrees(angle)
print(degree_angle)
'''
#2 RANDOM MODULE 
#random (including 0 but not 1)
'''import random 
num=random.random()
print(num)'''

#randint(including both a and b)
'''import random
num=random.randint(1,100)
print(num)'''

#
'''import random 
num=random.randint(1,10)
randum_number=int(input('enetr the number'))
if num==randum_number:
    print('congratulations')
else:
    print('better luck next time')'''

#
'''import random
guess_number=int(input('enter the number'))
random_number=random.randint(1,10)
attempts=5
for i in range(attempts):
    if guess_number==random_number:
        print('you won congratulations')
        break
    else:
        print('you lose,try again')
    if guess_number>random_number:
        print('too high')
    else:
        print('too low')
        guess_number=int(input('enter the number'))'''

#random uniform (including a but not b )
'''import random 
num=random.uniform(1,500)
print(num)'''

#random choice(such as a list,tuple and string)
'''import random
list1=[1,2,3,4,5,6,7]
for i in range(5):
    print(random.choice(list1))

tuple1=(1,2,3,4,5,6,7)
for i in range(5):
    print(random.choice(tuple1))

str1='hello world'
for i in range(5):
    print(random.choice(str1))'''


#take random single elements in str,tuple, and list 
'''import random
list1=random.choice([1,2,45,4,5,6,7,8])
print(list1)
tuple=random.choice((1,2,3,4,5,6,7,8))
print(tuple)
str1=random.choice(('hello world'))
print(str1)'''

#random shuffle list
'''import random
list1=[1,2,3,4,5,6,7,8,9]
random.shuffle(list1)
print(list1)'''

#random shuffle in tuple(must change tuple to list)
'''import random 
tuple1=(1,2,3,4,5,6,7,8)
list1=list(tuple1)
random.shuffle(list1)
print(list1)
'''
#random shuffle in set (must change set to list)
'''import random
set1={1,2,3,4,5,6,7,8,9}
list1=list(set1)
random.shuffle(list1)
print(list1)'''

#3 DATE AND TIME MODULE 

#datetime.date 

'''import datetime
x=datetime.date(2025,12,5)
print(x)'''

#datetime.time
'''import datetime
y=datetime.time(11,35,10,2)
print(y)'''

#datetime.datetime
'''import datetime
x=datetime.datetime.now()
print(x)
y=datetime.datetime.today()
print(y)'''

#
'''import datetime
z=datetime.datetime.now()
a=z.year
b=z.month
c=z.day
d=z.hour
e=z.minute
f=z.second
print('current year',a)
print('current month',b)
print('current day',c)
print('current hour',d)
print('current minute',e)
print('current second',f)'''

#strftime method
#current date and time 
'''from datetime import datetime
now=datetime.now()
t=now.strftime('%H:%M:%S')
print('time:',t)'''

#date and day format(month/day/year)
'''from datetime import datetime
now=datetime.now()
s1=now.strftime('%m/%d/%y,%H/%M:%S')
print('s1:',s1)'''

#date and year format(day/month/year)
'''from datetime import datetime
now=datetime.now()
s2=now.strftime('%d/%m/%y,%H:%M:%S')
print('s2:',s2)'''

'''from datetime import datetime
now=datetime.now()
s3=now.strftime('%Y/%m/%d')
print(s3)'''#2025/03/17

'''from datetime import datetime
now=datetime.now()
s4=now.strftime('%b/%D')
print(s4)'''#Mar/03/17/25

'''from datetime import datetime
now=datetime.now()
s5=now.strftime('%I:%M:%S:%p')
print(s5)'''#10:47:29:PM

'''from datetime import datetime
now=datetime.now()
s6=now.strftime('%H:%M:%S:%p')
print(s6)'''#22:48:50:PM

'''from datetime import datetime
now=datetime.now()
s7=now.strftime('its %A/%B/%D/%Y')
print(s7)
'''#its Monday/March/03/17/25/2025

'''from datetime import datetime
now=datetime.now()
s8=now.strftime('%j')
print(s8)'''#076

#strptime format 
'''import time
#get data of 4th april 2021 at time 9pm
print(time.strptime('04/04/21 09:31:22', '%d/%m/%y %H:%M:%S'))

#get data of 5th april 2021 at time 9pm 
print(time.strptime('05/04/21 09:00:42', '%d/%m/%y %H:%M:%S'))
'''

#time delta 
'''from datetime import datetime,timedelta
today=datetime.now()
future_date=today+timedelta(weeks=1,days=5,hours=2,minutes=10,seconds=30)
print(future_date)'''

#find age 
'''from datetime import datetime
dob='2002-09-27'
dob=datetime.strptime(dob,'%Y-%m-%d')
today=datetime.today()
age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
print(age)'''
