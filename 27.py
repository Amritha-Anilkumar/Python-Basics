'''a='10'
b=5
c=2.5'''
# convert a to int
#convert b to float and complex
#convert c to int

'''print(type(a))
print(type(b))
print(type(c))

inta=int(a)
print(type(inta))


floatb=float(b)
print(type(floatb))

complexb=complex(b)
print(type(complexb))

intc=int(c)
print(type(intc))'''
'''
NAME='AMRITHA'
intNAME=int(NAME)
print(type(NAME))
'''

'''a=input('enter a value')
b=input('enter a value')
sum=a+b
print(sum)'''

#AREA
'''r=float(input('enter a value'))
pi=float(input('enter value'))
area=pi*r*r
print(area)'''
        
'''n=int(input('enter a value'))'''
numbers=input('enter a number:')
place_names=['ones','tens','hundreds','thousands','ten thousands','lakhs','ten lakhs','crores']
length=len(numbers)
for i in range(length):
    digit=numbers[i]
    place=place_names[length-i-1]
    print(f"{digit} is in {place} place")



