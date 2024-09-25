def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            cipher_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            cipher_text += char  # Non-alphabetic characters remain unchanged
    return cipher_text

# Input from user
plain_text = input("Enter plain text: ")
shift = int(input("Enter shift value: "))

# Encrypting the plain text
cipher_text = caesar_encrypt(plain_text, shift)

# Displaying the results
print(f"Plain Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")
