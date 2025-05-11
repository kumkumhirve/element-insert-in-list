'''Q2: WAP to create list containing 10 elements , access each
elements of list by index &amp; loop?
'''
# Create a list with 10 elements
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Accessing elements by index:")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list[7])
print(my_list[8])
print(my_list[9])

print("\nAccessing elements using a loop:")
for index in range(len(my_list)):
    print(f"Element at index {index}: {my_list[index]}")
