#Program : To get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key Value")
for (key,value) in dict_num.items():
    print(key, " ",value)
print("Items : {}".format(dict_num.items()))