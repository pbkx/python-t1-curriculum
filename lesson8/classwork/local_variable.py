# Local variable: a variable made inside a function, that only exists inside a function.
def adopt_dog():
    pet = "dog"  # pet is a local variable
    print("the pet is", pet)

adopt_dog()

# Error: trying to use 'pet' outside its function
# print(pet)