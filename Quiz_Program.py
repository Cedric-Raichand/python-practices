# Simple Quiz Program in Python

score = 0

print("== Welcome to today's Quiz ==\n")


print("1. What is the capital of France?")
print("a) Berlin")
print("b) Paris")
print("c) Madrid")

answer = input("Your answer: ").lower()

if answer == "b" or answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")



print("2. Which language is used for web styling?")
print("a) CSS")
print("b) Python")
print("c) SQL")

answer = input("Your answer: ").lower()

if answer == "a" or answer == "css":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is CSS.\n")



print("3. What does CPU stand for?")
print("a) Central Process Unit")
print("b) Central Processing Unit")
print("c) Computer Personal Unit")

answer = input("Your answer: ").lower()

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.\n")



print("=== QUIZ COMPLETED ===")
print(f"You scored {score} out of 3!")
