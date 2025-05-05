
#check the reverse 1234
'''num=1234
rev=0
while num!=0:
    digit= num%10
    rev=rev*10+digit
    num=num//10
print(rev)
'''

#reverse 5678
'''num=5678
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
 '''

#reverse 1008
'''num=1008
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)'''

#pallindrome
num=3002
val=num
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(val)
if val==rev:
    print(rev,'is a pallindrome')
else:
    print('not a pallindrome')


#
num=101
val=num
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(val)
if val==rev:
    print(rev,'is a pallindrome')
else:
    print('not a pallindrome')

