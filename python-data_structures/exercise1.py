#!/usr/bin/python3

#Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_elements = l1[1::2]
print(odd_elements)

even_elements = l2[0::2]
print(even_elements)

new_list = odd_elements + even_elements

print(new_list)
