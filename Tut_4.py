#PYTHON TUPLES 
#THEY ARE ORDERED AND ARE UNCHANGED AND ARE INDEXED(ACCESED VIA INDEX IE TUPLE[0],[3]ETC)
#THEY ARE CREATED BY () BRACKETS

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#THEY ALLOW DUPLICATES
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)

#use the len() unction to get the number of items in a tuple 
print(len(thistuple2))

#Tuples can contain a single data type or can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Tuples are of type <class tuple> 
print(type(tuple1))

#check if an item is available in a tuple
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#To change/delete/add an item into atuple you first convert it to a list then perform your operations 
#then change it back to a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x=tuple(y)
print(x)

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#to delete the tuple we use the keyword del 
del tuple1

#Unpacking = here we are getting the items available in the tuple as Variables 
#NB: the number of variables should match the number of items in the tuple 
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#we use an * when we have fewer variables than items 
#when we use an * the variables are returned as a list
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2
print(green)
print(yellow)
print(red)

#looping through a tuple
for i in range(len(fruits2)):
  print(fruits2[i]) 

#while loop
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1 

#We use + to join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 

#we can multiply a tuple using *
print(tuple2 * 2)
