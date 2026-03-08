age = int(input("How old are you? "))
has_ticket = input("Do you have a movie ticket? (yes/no)")

if age >= 13 and has_ticket == "yes":  # AND: both conditions must be true for our code inside the if statement to run
    print("You can enter the PG-13 movie.")
else:
    print("You cannot enter the PG-13 movie.")
print("Movie check complete.")

has_pass = input("Do you have a pass? (yes/no) ")
has_coins = input("Do you have coins to pay? (yes/no) ")

if has_pass == "yes" or has_coins == "yes":  # OR: at least one condition must be true for our code inside the if statement to run
    print("You can ride the bus")
else:
    print("You cannot ride the bus")
print("Bus check complete.")

homework_done = input("Did you do your homework? (yes/no) ")
if not homework_done == "yes":  # NOT: flips True to False and False to True
    print("Go finish your homework!")
else:
    print("Good job! You're all done.")
print("Homework check complete.")

# You can combine multiple logical operators
is_raining = input("Is it raining? (yes/no) ")
has_umbrella = input("Do you have an umbrella? (yes/no) ")

if is_raining == "yes" and not has_umbrella == "yes":  # Order of operations: first not, then and, then or.
    print("Stay inside. You might get wet!")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside!")
else:
    print("No rain! You can go outside.")