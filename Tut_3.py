#Python Data Collection data types ie Tuple, Set, list, Dictionary

#1.List created via [] brackets
#List items are ordered(new items are added at the end of the list), changeable(can be edited), and allow duplicate values.
import this


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))#prints the number of items in a list

#It can consist of different data types
list1 = ["abc", 34, True, 40, "male"]#includes int, bool and string
print(list1)
print(type(list))#prints <class 'list'>

#You can create a list by using the list() constructor
thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist2)

#check if an item is in the list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the list")

#To change an item in the list we refer to the index
list1[2]= 55
print(list1)

#we can also change a range of items in the list 
thislist[1:3] = ["kiwi" , "mango"]
print(thislist)

#if you insert more values the range changes accordingly and vice versa and the length changes
thislist2[1:2] = ["car", "shoe", "spade"]
print(thislist2)
thislist2[1:3] = ["Feathers"]
print(thislist2)

#you can also use insert() method
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3)

#append() add items to the end of the list
thislist4 = ["toyota", "subaru", "mitsubishi"]
thislist4.append("nissan")
print(thislist4)

#extend() is used to combine lists and also list tothe other array types ie tuples, dictionaries etc
thislist3.extend(thislist4)
print(thislist3)

thistuple = ("fer", "ter")
thislist4.extend(thistuple)
print(thislist4)

#remove() removes a specified item 
thislist4.remove("fer")
print(thislist4)

#pop() removes the last item on the list or a specified index
thislist2.pop()
print(thislist2)

thislist3.pop(3)
print(thislist3)

#del keyword removes a specified index or deletes the whole list
del thislist#if you ty to print it will throw an error

#clear() empties the list
thislist2.clear()
print(thislist2)

#we use for and while loop to get items in an array

for i in range(len(thislist3)): print(thislist3[i])

thislist = ["apple", "banana", "cherry"]
x=0
while x < len(thislist):
    print(thislist[x])
    x=x+1

#code to set items with letter a into the newlist long hand 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#shorthand version requires data comprehesion
#syntax : newlist = [expression for item in iterable if condition == True]
newlist2=[]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

#sort() sorts the items in ascending order by default also numerically
thislist3.sort()
print(thislist3)

#to sort in descending order we set reverse=true in the sort method
thislist3.sort(reverse=True)
print(thislist3)

#you can aslso customize the sortiing by using key=function in the sort method
def myfunc(n):
  return abs(n - 50)

numlist = [100, 50, 65, 82, 23]
numlist.sort(key = myfunc)
print(numlist)#returns a list with the numbers closest to 50

#to sort a list with different cases we use key=str.lower
thislist5 = ["banana", "Orange", "Kiwi", "cheRry"]
thislist5.sort(key=str.lower)
print(thislist5)

#reverse() starts with the last item to th first
thislist5.reverse()
print(thislist5)

#to create a copy of a list we use copy() or list()

copylist=thislist5.copy()
print(copylist)

thislist5.reverse()
copylist2=thislist5.copy()
print(copylist2)