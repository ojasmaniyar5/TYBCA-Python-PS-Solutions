def count_case_characters(s):
    upper_case_count = sum(1 for char in s if char.isupper())
    lower_case_count = sum(1 for char in s if char.islower())
    
    print(f"No. of Upper case characters: {upper_case_count}")
    print(f"No. of Lower case characters: {lower_case_count}")

# Sample string
sample_string = 'The quick Brow Fox'
count_case_characters(sample_string)
