import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters  # lowercase and uppercase letters

    if include_digits:
        characters += string.digits  # include digits 0-9

    if include_special_chars:
        characters += string.punctuation  # include special characters

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
