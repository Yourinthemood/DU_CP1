# DU, Period 2, Caesar Cipher LAROSE

# Function to encode a message
def encode_message(text, shift_amount):
    # Start with empty result string
    result = ""
    # Look at each character in the message
    for char in text:
        # If it's a capital letter
        if char.isupper():
            # Convert letter to number code
            num = ord(char)
            # Add the shift to move forward
            num = num + shift_amount
            # If we go past Z, wrap around to A
            if num > 90:
                num = num - 26
            # Convert number back to letter and add to result
            result += chr(num)
        # If it's a lowercase letter
        elif char.islower():
            # Convert letter to number code
            num = ord(char)
            # Add the shift to move forward
            num = num + shift_amount
            # If we go past z, wrap around to a
            if num > 122:
                num = num - 26
            # Convert number back to letter and add to result
            result += chr(num)
        # If it's not a letter (space, punctuation, etc.)
        else:
            # Just add it without changing
            result += char
    return result

# Function to decode a message  
def decode_message(text, shift_amount):
    # Start with empty result string
    result = ""
    # Look at each character in the message
    for char in text:
        # If it's a capital letter
        if char.isupper():
            # Convert letter to number code
            num = ord(char)
            # Subtract the shift to move backward
            num = num - shift_amount
            # If we go past A, wrap around to Z
            if num < 65:
                num = num + 26
            # Convert number back to letter and add to result
            result += chr(num)
        # If it's a lowercase letter
        elif char.islower():
            # Convert letter to number code
            num = ord(char)
            # Subtract the shift to move backward
            num = num - shift_amount
            # If we go past a, wrap around to z
            if num < 97:
                num = num + 26
            # Convert number back to letter and add to result
            result += chr(num)
        # If it's not a letter (space, punctuation, etc.)
        else:
            # Just add it without changing
            result += char
    return result

# Ask user if they want to encode or decode a message
choice = input("Choose operation (1 for encode, 2 for decode): ")

# Ask user for the message they want to work with
message = input("Enter the message: ")

#  Ask user for the shift number (how many letters to move)
shift = int(input("Enter the shift value: "))

#  If user chose encode, call encode function
if choice == "1":
    encoded = encode_message(message, shift)
    print("Encoded message:", encoded)
#  If user chose decode, call decode function
elif choice == "2":
    decoded = decode_message(message, shift)
    print("Decoded message:", decoded)
# If user entered something else
else:
    print("Invalid choice. Please enter 1 for encode or 2 for decode.")
