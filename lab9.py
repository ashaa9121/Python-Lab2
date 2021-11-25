#Program : Find the index of an item of a tuple.

my_tuple = ('a','b','c','a','i','m','e')

#index of 'c'        result:2
print("Index of c : ",my_tuple.index('c'))

# Index of 'a' after 1st index               result:3 
print("Index of 'a' after 1st index is :",my_tuple.index('a',1))


# tuple_1 = ('a','b','c','d','e','f')
#print(tuple_1)
#string = input("Enter the char want to check:")
#try:
#	index = tuple_1.index(string)
#	print("Index of",string,"is",index)
#except Exception as e:
#	print("Input given is not in tuple")