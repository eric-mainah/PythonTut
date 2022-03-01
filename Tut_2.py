#Strings and Booleans in Python Methods/Edits

#Strings in Python are considered as arrays hence you can loop through them
x = " Joh,n Do,e "

print(x[2])#prints the second character of the string
print(len(x))#Prints the length of the string
print("Doe" in x)#checks if doe is in the string
print("Sarah" not in x)#checks if saraha is not in string
print(x[0:6])#Prints characters from the index1 to index6
print(x[0:])#prints characters from index1 to the last one
print(x[:8])#Prints from the first the index7
print(x.upper())#prints string to upper caes
print(x.lower())#prints string ro lower case
print(x.strip())#removes the white space before/after string
print(x.replace("o" , "e"))#replaces the character o to e
print(x.split(","))#splits the string at ,

#concatenating strings and integers use method format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#also can take unlimited number of arguments
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#for many arguments use indexes
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#booleans return true or false
print(10 > 9)# returns true
print(10 == 9)#returns false
print(10 < 9)#returns false

#Note all values that have content return true.Empty Sets,lists,tuples,0, all return false
bool(123)#returns true 
bool("")#returns false
