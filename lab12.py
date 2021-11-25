#Program : Write a Python program to convert a list of characters into a string.

my_list = ['e','d','a','b','c']

print("List : ",my_list)
print()
print("Type :", type(my_list))

# to covert character list to string...
print()
str = " "
for i in my_list:
    str = str +" "+ i

print("String : ", str)
print()
print("Type :",type(str))    