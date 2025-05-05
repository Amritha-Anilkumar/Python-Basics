'''x=10
if x>5:
    raise Exception('x should not exceed 5. the value of x was:{}'.format(x))'''

#execption handling 
'''numerator=10
denominator=0
result=numerator/denominator
print(result)'''#ZeroDivisionError: division by zero
'''try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print('denominator cannot be 0')'''


#
'''try:
    # even=[2,4,6,8]
    # print(even[5])
    a=5/0
    print(a)
except ZeroDivisionError:
    print('denominator cannot be 0')
except IndexError:
    print('index out of bound')'''

#else clouse(assert= check true or false)
'''try:
    num=int(input('enter the number'))
    assert num%2==0
except:
    print('not an even number')
else:
    reciprocal=1/num
    print(reciprocal)'''

#finally
'''try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print('error:denomintor cannot be 0')
finally:
    print('this is finally block')'''

# 
'''try:
    numerator=10
    denominator=5
    result=numerator/denominator    
except:
    print('error:denomintor cannot be 0')
else:
    print(result)
finally:
    print('this is finally block')'''

#
'''try:
    even=[2,4,6,8]
    print(even[2])
except IndexError:
    print('index out of bound')
else:
    print('access the element')
finally:
    print('this is finally block')'''

#
'''try:
    my_dict={'a':1,'b':2,'c':3}
    print(my_dict['c'])
except KeyError:
    print('key not found')
else:
    print('key found')
finally:
    print('this is finally block')'''


