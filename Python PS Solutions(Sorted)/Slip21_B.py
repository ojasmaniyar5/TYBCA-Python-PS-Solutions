# Original tuple of string values
original_tuple = (('333', '33'), ('1416', '55'))

# Convert to a tuple of integers
new_tuple = tuple(tuple(int(num) for num in sub_tuple) for sub_tuple in original_tuple)

# Print the new tuple
print("Original tuple values:", original_tuple)
print("New tuple values:", new_tuple)
