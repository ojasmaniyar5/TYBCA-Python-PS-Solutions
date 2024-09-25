def count_repeated_characters(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return {char: cnt for char, cnt in count.items() if cnt > 1}

# Sample string
sample_string = 'thequickbrownfoxjumpsoverthelazydog'
repeated_chars = count_repeated_characters(sample_string)

# Formatting the output
output = ', '.join(f"{char}-{cnt}" for char, cnt in repeated_chars.items())
print(output)
