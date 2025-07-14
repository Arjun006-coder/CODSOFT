import random

def generate_password(length):
    # Define characters manually
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    all_chars = lowercase + uppercase + digits + symbols

    password = ""
    for _ in range(length):
        password += random.choice(all_chars)

    return password

# Main program
print("Password Generator")
try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Please enter a number greater than 0.")
    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)
except ValueError:
    print("Invalid input")
