print("Enter the tree size: ")

size = int(input())

for row_num in range(1, size + 1):
    spaces = " " * (size - row_num)
    tree = "^" * (row_num * 2 - 1)
    print(spaces + tree)

spaces = " " * (size - 1)
print(spaces + "#")
print(spaces + "#")



## CHRISTMAS TREE PRINTER

# Instead of creating a plain tree like the one in the previous project, write a program that prints
# a program that prints a Christmas tree with "o" (ball) ornaments randomly replacing ^ branch 
# characters. For example, a Christmas tree of size 5 could look like this:

import random

print('Enter the tree size:')
size = int(input())

# Print the tree top:
for row_num in range(1, size + 1):
    spaces = ' ' * (size - row_num)
    tree = ''
    # Create the row from random 'o' and '^' characters:
    for branch_num in range(row_num * 2 - 1):
        if random.randint(1, 4) == 1:
            tree = tree + 'o'
        else:
            tree = tree + '^'
    print(spaces + tree)

# Print the tree trunk:
spaces = ' ' * (size - 1)
print(spaces + '#')
print(spaces + '#')
