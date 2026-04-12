print("My name is Max")  # print() is a function which has a string parameter

# Function that returns a greeting message
def make_greeting():
    greeting = "Hello, world!"
    return greeting

message = make_greeting()  # Call the make_greeting() function
print(message)

# Function that builds a face
def build_face():
    return ":)"

face = build_face()  # Call the build_face() function
print(face)

# Functions dont have to return anything
def print_poem():
    print("If I were a King,")
    print("I could do anything.")

# You can call functions as many times as you want
print_poem()
print_poem()

# Parameters are local variables that can only be accessed inside the function:
def personalized_greeting(name):  # name is a parameter
    return "Hello, " + name + "!"

personalized_message = personalized_greeting("Alice")
print(personalized_message)

# Function that returns a rectangles area based on length and width
def rectangle_area(length, width):  # length and width are parameters
    area = length * width
    return area

# When you call a function in a print statement, python will print what the function returns.
print("The area of a 5x3 rectangle is:", rectangle_area(5, 3))