# Program : Python program to sort a dictionary by key.

color_dict = {
              'red':'#FF0000',
              'green':'#008000',
              'black':'#000000',
              'white':'#FFFFFF'
              }
#dict items
items_color_dict  = color_dict.items()
print("Dictionary items : {}" .format(items_color_dict) )             

#after sorted dict items
sorted_color_dict = sorted(items_color_dict)
print("Sorted items : {}".format(sorted_color_dict))