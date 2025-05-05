

#BRAKE STATEMENT
'''n=10
while n>0:
   if n==5:
    break
   n-=1
   print(n)
print('Loop ended')'''

#continue
'''n=5
while n>0:
    n-=1
    if n==3:
        continue
    print(n)'''

#pass
'''n=5
while n>0:
    pass'''
    

    
#prime 

num = int(input('Enter a value: '))
i = 2
while i <= num // 2:
    if num % i == 0:
        print(num, 'is not prime')
        break
    i += 1
else:
    print(num, 'is prime')    
