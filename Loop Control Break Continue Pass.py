for i in range(5):
    if i == 3:
        break  # Exit loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip 3
    print(i)

for i in range(5):
    if i < 0:
        pass          # Empty placeholder for future code
    else:
        print(i)      # Just prints all numbers
# Output: 0, 1, 2, 3, 4

# Pass in a function stub
def my_function():
    pass              # Function to be implemented later