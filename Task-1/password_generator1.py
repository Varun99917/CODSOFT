import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
desired_length = int(input("Enter desired password length: "))
print("Your generated password is:", generate_password(desired_length))