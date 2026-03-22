numbers = [14, 1, 50, 4, 20, 12]

counter = 0  # Keeps track of how many numbers so far in my list are greater than 5

for i in range(len(numbers)):  # Looping through the list of numbers using an index
    item = numbers[i]  # Get the current item which we are on in the list
    if item > 5:  # Check if the current item is greater than 5
        counter = counter + 1  # If it is greater than 5, add 1 to the counter
print("There are", counter, "numbers greater than 5 in our list.")

animals = ["cat", "dog", "cat", "rabbit", "hamster", "dog", "cat"]

counter2 = 0  # Keeps track of how many times we see "cat" in our list

for i in range(len(animals)):
    item = animals[i]  # Get the current item which we are on in the list
    if item == "cat":  # Check if the current item is "cat"
        counter2 = counter2 + 1  # If it is "cat", add 1 to the counter 
print("There are", counter2, "cats in our list.")

num_cats = animals.count("cat")
print("There are", num_cats, "cats in our list.")