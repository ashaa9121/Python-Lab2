#Program : Write a Python program to generate all sublists of a list.

list1 = [1,2,3,4]
newlist = []
for i in range(len(list1)):
    n = i + 1
    while(n <= len(list1)):
        s = list1[i:n]
        newlist.append(s)
        n += 1

print("Sublist : " , newlist)                
