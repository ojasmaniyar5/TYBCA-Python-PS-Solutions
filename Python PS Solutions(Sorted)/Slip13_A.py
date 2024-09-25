def input_positive_integer():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            raise ValueError("The number must be positive.")
        print(f"You entered a valid positive integer: {num}")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Run the function
input_positive_integer()
