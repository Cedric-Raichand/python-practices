import math
password = input("Enter your password: ")
password = password.upper()
print("the first letter u entered is",password[0], "but dont worry, your full password is:", password )

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("hello", name)


x1 = int(input("Enter x1: "))
x2 = int(input("enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("enter y2: "))

print(x1)
print(x2)
print(y1)
print(y2)

answer = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
book = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print("Your answer is " +str(answer))
print("your answer is" , answer)
print("Your book is" , book)