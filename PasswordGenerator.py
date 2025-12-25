# Simple Random Password Generator
import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Random Password Generator!")

    while True:
        try:
            length = int(input("Enter the length of your password (e.g., 8, 12, 16): "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            password = generate_password(length)
            print(f"Your random password is: {password}\n")
        except ValueError:
            print("Please enter a valid number.")

        again = input("Do you want to generate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! Stay safe online!")
            break


if __name__ == "__main__":
    main()
