# input ALWAYS returns a string
user_input = input("Give me an integer:")
print(user_input)

# Error: cannot add integer to a string
# print(user_input + 1)

number = int(user_input)  # casting to an integer

user_number = int(input("Give me an integer:"))
print(user_number + 1)