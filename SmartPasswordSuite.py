import random
import re

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:',.<>?"

def generate_password():
    length = int(input("Enter desired password length (8–20): "))

    if length < 8 or length > 20:
        print("❌ Invalid length.")
        return

    all_chars = LOWER + UPPER + DIGITS + SYMBOLS
    password = "".join(random.choice(all_chars) for _ in range(length))

    print("✅ Generated Password:", password)


def test_password():
    password = input("Enter password to test: ")

    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[^a-zA-Z0-9]", password): score += 1

    print("\n📊 Password Strength:")

    if score <= 2:
        print("WEAK 😬")
        print("Tip: Use longer password with symbols.")
    elif score <= 4:
        print("MEDIUM ⚠️")
        print("Tip: Mix uppercase, numbers & symbols.")
    else:
        print("STRONG 🔥")
        print("Excellent password ✔️.")


def main():
    while True:
        print("\n🔐 SMART PASSWORD SUITE")
        print("1. Generate Random Password")
        print("2. Test Password Strength")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_password()
        elif choice == "2":
            test_password()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
