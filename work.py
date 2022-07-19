
#local and global varibale and global varibale
from re import A


a=10
def f():
  print("insidef():",a)
def g():
  a=20
  print("inside h():",a)
def h():
  global a  
  a=30
  print("inside h():",a)
print("global:",a)
f()
print("global:",a)
g()
print("global:",a)
h()
print("global:",a)
#class and object


#simple class
class a :
  a=5
  print(a)
  #class with object
  class a:
    x=5
  p = a()
  print(p.x)

#constructor
class A:
  def __init__(self):
    print("hii")
  def f1(self):
    print("helllo")
obj=A()
obj.f1()    

#constructor with Argument
class A:
  def __init__(self,a,b):
    print(a+b)
  def f1(self,a,b):
    print(a+b)
obj=A(5,4)
obj.f1(10,2) 


# star pattern
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

for i in range(4):
    for j in range(4):
        print("* ", end="")
    print("\n")
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

#program for wheather a number is palindrome number
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
 dig=num%10
 rev=rev*10+dig
 num=num//10
if(temp==rev):
 print("The number is palindrome!")
else:
 print("Not a palindrome!")

# Program to check if a string is palindrome or not

my_str = input("enter the string")
my_str = my_str.casefold()
print(my_str)
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
# list

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# slicing string
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#remove function
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# set
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)


fruits = {"apple", "banana", "cherry"}

fruits.clear()


print(fruits)
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

fruits = {"apple", "banana", "cherry"}


fruits.remove("banana")

print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


fruits = {"apple", "banana", "cherry"}
frozenset(fruits)
print(type(fruits))


# dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#function
def name():
  print("Hello from a function")

name()
# with argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")