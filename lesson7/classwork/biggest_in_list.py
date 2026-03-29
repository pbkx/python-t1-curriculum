numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# You can use built-in Python functions to find the biggest and smallets numbers in a list.
biggest_item = max(numbers)
smallest_item = min(numbers)

print("The biggest item in the list is:", biggest_item)
print("The smallest item in the list is:", smallest_item)

print("Our algorithm:")

biggest = numbers[0]  # Start by assuming the first item is the biggest
for i in range(len(numbers)):  # Go throough each item in the list
    if numbers[i] > biggest:  # Check if the current item is bigger than the biggest item we've seen so far
        biggest = numbers[i]  # If we find a bigger item, update biggest to be that item
print("The biggest item in the list is:", biggest)