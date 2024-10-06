#1. Write Code on a white board or paper

#2. Know Control Flow

for i in range(1, 11):
print(i)

i = 1
while i <= 11:
    print(i)
    i += 1
else:
    print(i)

a = 10
b = 20
if a < b :
    print ('{} is less than {}'.format(a, b))
elif a == 20:
    print("{} is equal to {}".format(a,b))
else:
    print("{} is greater than {}".format(a,b))
	

#3. Past Project
   #Some kind of utilty project
   
#4. Common interview problem
  
  #Prime Numbers


#fizzbuzz
for num in range(1,100):
    if num % 5 == 0 and num % 3 == 0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 == 0:
        print(num, "Buzz")
    else:
        print(num)

#Fibanoocci series
Count = 10
a, b = 0, 1
for i in range(0, Count):
    print(a)
    a, b = b, a + b
	
#5. Basic Data Type
my_list = [1 ,2 ,3, 4, 5]
for lis in my_list:
    print(lis)

my_tup = (6, 7, 8, 9, 10)
for tup in my_tup:
    print(tup)

dict = {'Name': 'Samsheer', 'Age': 40, 'Profession' : 'IT'}
for item, value  in dict.items():
    print(item, value)

set = {10, 20, 30, 40, 50}
for item in set:
    print(item)

tuple is immutable

#6 - List comprehension
my_list = [1 ,2 ,3, 4, 5]
my_new_list = [i*i for i in my_list]
print(my_new_list)


#7 Generators
def fib(count):
    a, b = 0, 1
    for i in range(0, count):
        yield "{}: {}".format(i+1 ,a)
        a, b = b, a + b
for i in fib(10):
    print(i)
	
#8 OOP Basics
class Person():
    def __init__(self,name):
        self.name = name
    def reveal_identity(self):
        print(f"my name is {self.name}")
class Superhero(Person):
    def __init__(self,name, super_hero):
        super(Superhero,self).__init__(name)
        self.super_hero = super_hero
    def reveal_identity(self):
        super(Superhero,self).reveal_identity()
        print(f"my Superhero is {self.super_hero}")

p = Person('Samsheer')
p.reveal_identity()

p1= Superhero('Jack' ,'Spyderman')
p1.reveal_identity()

#9 ask python related qn to interviewer that u are really strong


#10
basics of other technologies
