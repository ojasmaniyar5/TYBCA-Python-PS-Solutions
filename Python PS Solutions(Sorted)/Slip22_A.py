class Repeater:
    def __init__(self, string):
        self.string = string

    def __mul__(self, n):
        return self.string * n

# Accept input from user
user_string = input("Enter a string: ")
n = int(input("Enter a number: "))

# Create a Repeater object
repeater = Repeater(user_string)

# Display the repeated string
result = repeater * n
print(result)
