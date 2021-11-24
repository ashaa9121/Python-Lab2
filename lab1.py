# Program: To create all possible strings by using 'a', 'e', 'i', 'o', 'u'. 
# Use the characters exactly once.

import random
a = ['a','e','i','o','u']
random.shuffle(a)
print(''.join(a))
