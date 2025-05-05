'''for i in range(1,5):
    for j in range(1,5):
        print(i,j)

'''

'''for i in range(5):
    for j in range(5):
        print('*',end='')
    print()
    '''

#Rectangle
'''for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#
'''for i in range(5):
    for j in range(5):
        if i==2 or j==2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit-1 or j==limit-1:
            print('💗',end='')
        else:
            print(' ',end='')
    print()
'''
#
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==limit//2 or j==limit//2:
            print('💗',end='')
        else:
            print(' ',end='')
    print()'''

#X
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==j or i+j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#7
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#7/
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or i+j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#Z
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or i+j==limit-1 or i==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#rectangle with / 
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i+j==limit-1 or i==limit-1 or j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==j or i+j==limit-1 or i==limit-1 or j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#J

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==limit//2 and i!=limit-1 or i==limit-1 and j<limit//2 and j!=0 or j==0 and i>limit//2 and i!=limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
            
#A

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or j==limit-1 or i==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#A
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=0 and j!=limit-1 or  j==0 and i!=0 or j==limit-1 and i!=0 or i==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        
'''
# B

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit-1 or i==limit//2 or j==limit-1:
             print('*',end='')
        else:
            print(' ',end='')
    print()'''
#B
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=limit-1 or j==0 or i==limit-1 and j!=limit-1 or i==limit//2 and j!=limit//2 or j==limit-1 and i!=0 and i!=limit-1:
             print('*',end='')
        else:
            print(' ',end='')
    print()'''
        
#C

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#C
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=0 or j==0  and i!=0 and i!=limit-1 or i==limit-1 and j!=0:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#D
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit-1 or j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        '''
#D
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=limit-1 or j==0 and i!=limit-1 or i==limit-1 and j!=limit-1 or j==limit-1 and i!=0 and i!=limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#E
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit-1 or i==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
            


# F
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==0 or i==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#G
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=0 or j==0 and i!=0 and i!=limit-1 or i==limit-1 and j!=0 or j==limit-1 and i>=limit//2 or i==limit//2 and j>=limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#H
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==0 or j==limit-1 or i==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
#I
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or i==limit-1 or j==limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#J
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 or j==limit//2 and i!=limit-1 or i==limit-1 and j<limit//2 and j!=0 or j==0 and i>limit//2 and i!=limit-1 :
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#K
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==limit//2 or i+j==limit-1 and j!=0 and i<=j or i==j and i>limit//2 and j>limit//2:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
           

#L
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==0 or i==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

'''
#M
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==0 or j==limit-1 or i==j and i<limit//2 and j<limit//2 or i+j==limit-1 and i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
       
       
#N
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if j==0 or i==j or j==limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#O
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit):
        if i==0 and j!=0 and j!=limit-1 or j==0 and i!=0 and i!=limit-1 or i==limit-1 and j!=limit-1 and j!=0 or j==limit-1 and i!=0 and i!=limit-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
'''
#P
