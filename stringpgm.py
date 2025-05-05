'''name='AMRITHA'
 print(name)'''


'''multi_line='hii hellooo dfghhjjkkkkksdfghjSasdfghj'
print(multi_line)'''

'''for chr in name:
    print(chr)
 print(len(name))'''

'''txt='The best things in life are free'
print('free' in txt)
print('e' in txt)
print('expensive'not in txt)'''

'''b='Hello, World!'
print(b[2:-2])
print(name[::-1])'''

'''a='Hello,World!'
print(a.upper())
print(a.lower())'''

'''a='    hello,world     '
print(a)
print(a.strip())
#ans hello,world(for space remove)'''

'''a='hello, word'
print(a.replace('h','j'))
print(a.replace('o','w'))'''

'''a='hel,lo, w,orld'
print(a.split(','))
print(a.split('w'))'''

'''txt='this is a dummy text helloo hii we'
words=txt.split()
print(words)
print(len(words))'''

'''txt='this is a dummy text Helloo hii we'
words=txt.split()
for i in words:
     if i[0]=='h' or i[0]=='H':
         print(i)'''

'''a='AMRITHA'
b='P'
print(a+ b)

name='Amritha'
place='calicut'

"""a='My name is {}. I am from {}'
print(a.format(name,place))
"""
print(f'My name is {name}. I am from {place}')
name='AMRITHA'
age=22
a='my name is {}. i am {}'
print(f'my name is {name} and i am {age}')
print(a.format(name,age))
txt="I am \"Amritha\" greeting you"
print(txt)'''

'''txt='it\'s alright'
print(txt)
#new line represent n 
txt2="Hello\nworld"
print(txt2)'''

#4 tab represent t 

'''txt3="hello\tworld"
print(txt3)
txt="hello,and.welcome to my world"
x=txt.capitalize()
print(x)'''


'''txt="hello,and.Welcome to My world"
x=txt.capitalize()
print(x)'''
#CASEFOLD 
'''txt='HELLO WORLD'
print(txt.casefold())'''

#Center 
'''name='AMRITHA'
x=name.center(25,'!')
print(x)'''

#Count
'''txt1='hello,and. welcome to my world'
print(txt1.count('o',1,10))'''
#endswith 
'''print(txt1.endswith('world'))'''
#index
'''print(txt1.index('w'))
print(txt1.index('w'))
'''

# #
'''print(txt1.find('w'))
print(txt1.find('z'))
isalnm-check the aphabets and numbers 
a='name'
b=a.isalnum()
print(b)'''

'''a='name123'
b=a.isalnum()
print(b)
'''
'''a='name123, ' 
b=a.isalnum()
print(b)
'''
'''a='12345'
b=a.isalnum()
print(b)
'''
'''isalpha-check the aiphabets only 
a='name'
b=a.isalnum()
print(b)
a='name123'
b=a.isalnum()
print(b)'''

'''a='name*@'
b=a.isalnum()
print(b)'''

'''isdigit-check check the digit only 
a='1234'
b=a.isdigit()
print(b)
'''
'''a='name'
b=a.isdigit()
print(b)'''

'''a='name1234'
b=a.isdigit()
print(b)'''

#islower-check lowercase and number 
'''a='name'
b=a.islower()
print(b)'''

'''a='NAme'
b=a.islower()
print(b)'''

'''a='name123'
b=a.islower()
print(b)'''

#isupper-check the uppercase and number 
'''a='NAME'
b=a.isupper()
print(b)
'''
'''a='name'
b=a.isupper()
print(b)'''

'''a='NAME1234'
b=a.isupper()
print(b)'''

# #title 
'''a='my name is amritha.i am from calicut. my fathers name is anilkumar'
print(a.title())'''

# #swapcase
'''a='my NAME is amritha. i am from calicut.my fathers name is anilkumar'
print(a.swapcase())'''

'''a='hello, word'
print(a.replace('h','j'))
print(a.replace('o','w'))
'''

#maketrans
'''txt='sunday is holiday'
mytrans=txt.maketrans('s','p')
print(mytrans)
# print(txt.translate(mytrans))'''

#JOIN 
'''a='a hellooo hii world good morning'
sp=a.split()
print(sp)
print('#'.join(sp))
print(''.join(sp))
'''


'''txt='ilove apples,apples are my favourate fruite'
x=txt.count('apple')
print(x)'''

'''a='my name is amritha.i am from calicut. my fathers name is anilkumar'
print(a.title())'''

'''a='name1234'
b=a.isdigit()
print(b)'''

'''name='AMRITHA'
age=22
a='my name is {}. i am {}'
print(f'my name is {name} and i am {age}')
print(a.format(name,age))'''