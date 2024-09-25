class StringManipulation:
    def __init__(self, string):
        self.string = string

    def reverse_words(self):
        reversed_string = ' '.join(reversed(self.string.split()))
        return reversed_string

# Example usage
obj = StringManipulation("Hello world this is Python")
print(obj.reverse_words())
