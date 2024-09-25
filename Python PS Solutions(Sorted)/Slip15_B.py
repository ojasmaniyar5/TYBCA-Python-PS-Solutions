def remove_odd_index_chars(input_string):
    return ''.join(char for index, char in enumerate(input_string) if index % 2 == 0)

# Accept input from the user
user_input = input("Enter a string: ")
result = remove_odd_index_chars(user_input)

print(f"String after removing characters at odd index values: {result}")
