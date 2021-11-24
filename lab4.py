# Program : To count repeated characters in a string.

string = input("Enter a string:")
repeated_char = {}
for i in string:
    if(i in repeated_char):
        repeated_char[i]+= 1
    else:
        repeated_char[i] = 1
       
for key in repeated_char:
  if repeated_char[key] > 1:
    print(key , repeated_char[key])  

