# Input: upper limit n
n = int(input("Enter a number (n): "))

# Generate dictionary
squared_dict = {x: x*x for x in range(1, n + 1)}

# Print the dictionary
print(squared_dict)
