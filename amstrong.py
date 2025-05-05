'''num=input('enter a value')
len=len(num)
sum=0
i=0
while i<len:
    intnum=int(num[i])
    sum=sum+intnum**len
    i=i+1
if int(num)==sum:
    print('num is amstrong')
else:
    print('num is not amstrong')'''

num=input('enter value')
len=len(num)
sum=0
i=0
while i<len:
    intnum=int(num[i])
    sum=sum+intnum**len
    i=i+1
if int(num)==sum:
    print('num is amstrong')
else:
    print('num is not amstrong')


