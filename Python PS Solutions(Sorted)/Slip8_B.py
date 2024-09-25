class StringManipulation:
    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())
    
    def reverse_and_lower(self):
        reversed_string = ' '.join(reversed(self.string.split()))
        print(reversed_string.lower())

# Create an object of the class
obj = StringManipulation()
obj.get_String()
obj.print_String()  # Print in uppercase
obj.reverse_and_lower()  # Print reversed string in lowercase
