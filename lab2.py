# Program : To count the number of characters (character frequency) in a string.

input_string = "python program"
frequencies = {} 
  
for i in input_string: 
   if i in frequencies: 
      frequencies[i] += 1
   else: 
      frequencies[i] = 1

print("Character frequecy in {} is: \n{}".format(input_string, frequencies))