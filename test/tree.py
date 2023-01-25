#!/usr/bin/python3

#prompt user to enter the size of the tree

tree_height = input('Enter the size of the tree: ')

#convert tree size into an integer

tree_height = int(tree_height)

#define spaces
spaces = tree_height - 1

#define hashes
hashes = 1

#save stamp spaces
stamp_spaces = tree_height - 1

#use while loop

while (tree_height != 0):

#print spaces
    for i in range (spaces):
        print(' ', end="")

#print hashes
    for i in range (hashes):
        print('#', end="")
#print a new line
    print()

#decreament spaces
    spaces -= 1

#increament hashes
    hashes += 2

#decreament trees
    tree_height -= 1

#print save stump
for i in range(stamp_spaces):
    print(' ', end="")
print('#')




