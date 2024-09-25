class StringManipulation:
    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())

# Create an object of the class
obj = StringManipulation()
obj.get_String()
obj.print_String()
