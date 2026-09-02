print("Enter the tree size: ")

size = int(input())

for row_num in range(1, size + 1):
    spaces = " " * (size - row_num)
    tree = "^" * (row_num * 2 - 1)
    print(spaces + tree)

spaces = " " * (size - 1)
print(spaces + "#")
print(spaces + "#")





