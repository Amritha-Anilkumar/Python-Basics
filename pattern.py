'''print(ord('a'))
print(ord('B'))
print(ord('C'))
print(ord('z'))
for i in range(97,123):
    print(chr(i))
'''












'''limit = int(input('Enter a value: '))


for i in range(limit):
    for j in range(i):
        print(' ', end='')
    for k in range(2 * (limit - i) - 1):  
        print('*', end='')
    print()


for i in range(limit - 2, -1, -1):  
    for j in range(i): 
        print(' ', end='')
    for k in range(2 * (limit - i) - 1):  
        print('*', end='')
    print()'''


'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print('*',end='')
    print()
*
**
***
****
*****
******
'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(chr(65+j),end='')
    print()

A
AB
ABC
ABCD
ABCDE
ABCDEF'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(chr(96+i),end='')
    print()
a
bb
ccc
dddd
eeeee
ffffff
'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(i,end='')
    print()'''
'''
1
22
333
4444
'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(j+1,end='')
    print()
ans
1
12
123
1234'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(65+i),end='')
    print()
AAAAAAA
BBBBBB
CCCCC
DDDD
EEE
FF
G'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(65+j),end='')
    print()
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(96+i),end='')
    print()
aaaaaa
bbbbb
cccc
ddd
ee
f
'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(96+j),end='')
    print()

abcdef
abcde
abcd
abc
ab
a
'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(2*i+1):
         print(chr(96+i),end='')
    print()
aaa
bbbbb
ccccccc
ddddddddd
eeeeeeeeeee
fffffffffffff
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(2*i+1):
         print(chr(96+j),end='')
    print()
ab
`abcd
`abcdef
`abcdefgh
`abcdefghij
`abcdefghijkl
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(2*i+1):
         print(chr(65+j),end='')
    print()
A
ABC
ABCDE
ABCDEFG
ABCDEFGHI
ABCDEFGHIJK
ABCDEFGHIJKLM
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(2*i+1):
         print(chr(65+i),end='')
    print()
A
BBB
CCCCC
DDDDDDD
EEEEEEEEE
FFFFFFFFFFF
GGGGGGGGGGGGG'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(65+j),end='')
    print()
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(65+i),end='')
    print()
AAAAAAA
BBBBBB
CCCCC
DDDD
EEE
FF
G
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(96+j),end='')
    print()
abcdef
`abcde
`abcd
`abc
`ab
`a
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(chr(96+i),end='')
    print()
aaaaaa
bbbbb
cccc
ddd
ee
f'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print('*',end='')
    print()
ans
*****
****
***
**
*'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(2*i+1):
         print('*',end='')
    print()
ans
*
***
*****
*******
*********'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()
ans
    *
   **
  ***
 ****'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(' ',end='')
    for k in range(2*i+1):
        print(chr(96+i),end='')
    print()
      aaa
     bbbbb
    ccccccc
   ddddddddd
  eeeeeeeeeee
 fffffffffffff'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(' ',end='')
    for k in range(2*i+1):
        print(chr(96+j),end='')
    print()
       f
      eee
     ddddd
    ccccccc
   bbbbbbbbb
  aaaaaaaaaaa
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(' ',end='')
    for k in range(2*i+1):
        print(chr(65+i),end='')
    print()
       A
      BBB
     CCCCC
    DDDDDDD
   EEEEEEEEE
  FFFFFFFFFFF
 GGGGGGGGGGGGG
limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(' ',end='')
    for k in range(2*i+1):
        print(chr(65+j),end='')
    print()
       G
      FFF
     EEEEE
    DDDDDDD
   CCCCCCCCC
  BBBBBBBBBBB
 AAAAAAAAAAAAA'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
         print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()'''
'''ans
     *
    ***
   *****
  *******
 *********'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(' ',end='')
    for k in range(limit-i):
        print('*',end='')
    print()'''
'''ans
*****
 ****
  ***
   **
    *
'''

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
         print(' ',end='')
    for k in range(limit-i*2):
        print('*',end='')
    print()

*****
 ***
  *
'''
#
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print('*',end='')
    print()
for i in range(limit):
    for j in range(limit-i):
        print('*',end='')
    print()
    
*
**
***
****
*****
****
***
**
*
'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(chr(96+i),end='')
    print()
for i in range(limit):
    for j in range(limit-i):
        print(chr(96+i),end='')
    print()
a
bb
ccc
dddd
eeeee
ffffff
```````
aaaaaa
bbbbb
cccc
ddd
ee
f

limit=int(input('enter a value'))
for i in range(limit):
    for j in range(i):
        print(chr(65+i),end='')
    print()
for i in range(limit):
    for j in range(limit-i):
        print(chr(65+i),end='')
    print()
B
CC
DDD
EEEE
FFFFF
GGGGGG
AAAAAAA
BBBBBB
CCCCC
DDDD
EEE
FF
G
   
'''
#

'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()
for i in range(limit):
    for j in range(i):
        print(' ',end='')
    for k in range(limit-i):
        print('*',end='')
    print()

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(i):
        print(chr(97+j),end='')
    print()
for i in range(limit):
    for j in range(i):
        print(' ',end='')
    for k in range(limit-i):
        print(chr(97+j),end='')
    print()
      f
     ee
    ddd
   cccc
  bbbbb
 aaaaaa
aaaaaaa
 aaaaaa
  bbbbb
   cccc
    ddd
     ee
      f
    '''

#
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
for i in range(limit):
    for j in range(i+2):
        print(' ',end='')
    for k in range(limit-i*2):
        print('*',end='')
    print()

    *
   ***
  *****
 *******
  *****
   ***
    *
 '''
'''limit=int(input('enter a value'))
for i in range(limit):
    for j in range(limit-i):
        print(' ',end='')
    for k in range(2*i-1):
        print(chr(97+j),end='')
    print()
for i in range(limit):
    for j in range(i+2):
        print(' ',end='')
    for k in range(limit-i*2):
        print(chr(97+j),end='')
    print()
      f
     eee
    ddddd
   ccccccc
  bbbbbbbbb
 aaaaaaaaaaa
  bbbbbbb
   ccccc
    ddd
     e
     '''
#

    

    

        
        
        
        
        
