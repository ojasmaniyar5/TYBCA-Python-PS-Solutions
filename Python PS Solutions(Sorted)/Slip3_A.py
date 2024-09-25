my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'
new_key, new_value = 'd', 4

if key_to_check in my_dict:
    my_dict.pop(key_to_check)  # Remove the existing key
    my_dict[new_key] = new_value  # Add the new key-value pair

print(my_dict)
