# Program : Password generator in Python.

import random
import string

length = 20
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation

#combination of data
all = lower + upper + num + symbol
temp = random.sample(all,length)

#create the password
password = ''.join(temp)
print("Your new password :")
print(password)

