'''def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
f=factorial(5)
print(f)'''

'''class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class shoppingcart:
    def __init__(self):
        self.items=[]
    def add_product(self,product):
        self.items.append(product)
    def total_price(self):
        return sum(item.price for item in self.items)
    def show_cart(self):
        for item in self.items:
            print(f"{item.name}:${item.price}")
        print(f"Total:${self.total_price()}")
cart=shoppingcart()
cart.add_product(product("shoes",50))
cart.add_product(product("T-shirt",20))
cart.show_cart()'''

'''class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def _str_(self):
        return f"username:{self.username}"
users= [
    User("john","password123"),
    User("jane","user123"),
    User("admin","admin123")
]
for user in users:
    print(user)'''

'''class BankAccount:
    def _init_(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Balance for {self.holder_name}: ${self.balance}")


account =BankAccount("123456", "Alice")
account.deposit(1000)
account.withdraw(500)
account.check_balance()
        '''

'''class Employee:
    def __init__(self,name,basic_salary,hra,da):
        self.name=name
        self.basic_salary=basic_salary
        self.hra=hra
        self.da=da
    def calculate_salary(self):
        total=self.basic_salary+self.hra+self.da
        print(f"{self.name}'s total salary:{total}")
emp=Employee("john",30000,5000,2000)
emp.calculate_salary()'''

'''class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def '''
'''class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):  # fixed here
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):  # fixed here
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle Area: {rect.area()}")
print(f"Circle Area: {circle.area()}")'''

'''class Student:
    def __init__(self, name, marks):  # fixed __init__
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        average = sum(self.marks) / len(self.marks)
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"{self.name}'s Grade: {grade}")


student = Student("Alice", [85, 92, 78, 88])
student.calculate_grade()
'''
'''class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookStall:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} - ${book.price}")

    def total_cost(self):
        total = sum(book.price for book in self.books)
        print(f"Total Cost: ${total}")


stall = BookStall()
stall.add_book(Book("Python Basics", "Guido", 25))
stall.add_book(Book("Learn Django", "Adrian", 30))
stall.display_books()
stall.total_cost()'''

'''class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            rate = 1.5
        elif self.units <= 200:
            rate = 2.5
        else:
            rate = 3.5
        bill_amount = self.units * rate
        print(f"{self.customer_name}'s Electricity Bill: ${bill_amount}")


bill = ElectricityBill("Alice", 180)
bill.calculate_bill()'''

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1

class VotingSystem:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, name):
        if name not in self.candidates:
            self.candidates[name] = Candidate(name)

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name].add_vote()
            print(f"Vote casted to {name}")
        else:
            print("Candidate not found.")

    def show_results(self):
        print("\nVoting Results:")
        for candidate in self.candidates.values():
            print(f"{candidate.name}: {candidate.votes} votes")

# Example
system = VotingSystem()
system.add_candidate("Alice")
system.add_candidate("Bob")
system.add_candidate("Charlie")

system.vote("Alice")
system.vote("Bob")
system.vote("Alice")
system.vote("Charlie")
system.vote("Alice")

system.show_results()




        