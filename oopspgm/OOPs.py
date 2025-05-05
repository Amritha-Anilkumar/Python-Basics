#create an obeject
'''class myclass:
       x=5
       z=5
       y='amritha'
       def add(self):
              return 10
p1=myclass()
p2=myclass()
print(p1.x)
print(p1.y)
print(p1.add())
print(p2.add())'''
#object method(__init__)special functions, constructors, not required to call the function 
'''class myclass:
       def __init__(self,name,age):
         self.name=name
         self.age=age
       def helloworld(self):
              print('hello my name is'+ ' '+self.name)
p1=myclass('john',30)
p1.helloworld()
p2=myclass('amritha',22)
p2.helloworld()'''


# single inheritence 
'''class animal:
    def speak(self):
        print('animal speaking')
class dog(animal):
    def bark(self):
        print('dog barking')
d=dog()
d.bark()
d.speak()'''

#Multi level inheritence 
'''class animal:
    def speak(self):
        print("Animal speaking")
class dog(animal):
    def bark(self):
        print("dog barking")
class dogChild(dog):
    def eat(self):
        print("eating bread")
d=dogChild()
d.bark()
d.speak()
d.eat()'''

#Multiple  inheritence
'''class calculation1:
    def summation(self,a,b):
        return a+b
class calculation2:
    def multiplication(self,a,b):
        return a*b
class calculation3(calculation1,calculation2):
    def divide(self,a,b):
        return a/b
d=calculation3()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))'''
    
#hierarchical inheritance
'''class parent:
    def func1(self):
        print("this function is in parent class")
class child1(parent):
    def func2(self):
        print("this function is in child1")
class child2(parent):
    def func3(self):
        print("this function is in child2")
object1=child1()
object2=child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()'''

#Hybrid inheritance
'''class school:
    def func1(self):
        print("this function is in school")
class student1(school):
    def func2(self):
        print("this function is in student1")
class student2(school):
    def func3(self):
        print('this function is in student2')
class student3(student1,school):
    def func4(self):
        print('this function is in student 3')
object=student3()
object.func1()
object.func2()  
object.func4()'''


#Encapsulation 
'''class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of india")
    def type(self):
        print("India is a devoloping country")
class USA():
    def capital(self):
        print("Washington,D.C.is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")
obj_ind=India()
obj_ind.type()
obj_ind.capital()
obj_ind.language()
obj_usa=USA()
obj_usa.type()
obj_usa.capital()
obj_usa.language()'''
'''for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()'''

#overriding 
'''class animal:
    def speak(self):
        print('speaking')
class dog(animal):
    def speak(self):
        print("barking")
d=dog()
d.speak() '''

#super class
'''class mammal:
    def speak(self):
        print("mammal class")
class human(mammal):
    def speak(self):
        print("human class")
        super().speak()
d=human()
d.speak()'''

#
#parent class 
'''class vehicle():
    def __init__(self,model,colour):
        self.model=model
        self.colour=colour
    def display(self):
        return f"{self.model} {self.colour}"
#child class inheriting from vehicle
class car(vehicle):
    def ___init___(self,model,colour):
        super().___init___(model,colour) #parent constructer
    def display(self):
        return f"{self.model} {self.colour}"
class motorcycle(vehicle):
    def ___init___(self,model,colour):
        super().___init___(model,colour)
    def display(self):
        return f"{self.model} {self.colour}"
my_car=car('Toyota','Black')
print(my_car.display())

my_motoercycle=motorcycle('Honda','Red')
print(my_motoercycle.display())'''

#POLYMORPHISM 
'''class animal:
    def sound(self):
        print('animal sound')
class cat(animal):
    def sound(self):
        print('meow')
class dog(animal):
    def sound(self):
        print('bark')
dog=dog()
cat=cat()
animals=[dog,cat]
for animal in animals:
    animal.sound()'''

#DATA ABSTRACTION 
from abc import ABC 
#abtract base class
class shape(ABC):
    def area(self):
        return None
    def perimeter(self):
        return None 
class circle(shape):
    def ___init___(self,radious):
        self.radious=radious
    def area(self):
        return 3.14*self.radious*self.radious
    def parimeter(self):
        return 2*3.14*self.radious
class rectangle(shape):
    def ___init___(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
circle=circle(5)
rectangle=rectangle(4,6)
print('circle are:',circle.area())
print('circle parimeter:',circle.perimeter())
print('rectangle area:',rectangle.area())
print('rectangle:',rectangle.perimeter())






