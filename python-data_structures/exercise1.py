#!/usr/bin/python3
#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the secon

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

result = list1[1::2]
print(result)

result2 = list2[0::2]
print(result2)

res = list()

res.extend(result)
res.extend(result2)

print(res)

#concantenation produces same results

output = result + result2

print(output)
