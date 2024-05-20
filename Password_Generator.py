import random
import string
def generate_password(length, use_uppercase, use_digits, use_symbols):
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''


    all_characters = lowercase_letters + uppercase_letters + digits + symbols


    if not all_characters:
        raise ValueError("No character types selected for password generation")

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be greater than 0")

            use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
            use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

            password = generate_password(length, use_uppercase, use_digits, use_symbols)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(f"Invalid input: {e}")

        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
