
utensils = {"knife","spoon","fork","ladel"}
dishes = {"napkin","bowl","plate","cup"}
utensils.update(dishes)
print(utensils)
print()
for i in utensils:
    print(i)
print()
dinner = utensils.union(dishes)
print(dinner)
print()
for i in dinner:
    print(i)
print()

capitals = {"usa":"washington dc",
            "india":"new delhi",
            "china":"new york",
            "russia":"manager"}

print(capitals["russia"])
print(capitals.get("YUK"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals)
print(capitals.pop("china"))

for key,values in capitals.items():
    print(key,values)

print()


name = "bro code"
if name[0].islower():
  print(name.capitalize())
print(name[0:3].upper())
print(name.upper())

print()




def hello(you,name):
    print("cedric is the best" , you , name)
    print("that's good")
hello("bro","and so")

def multiply (number1,number2):
    result=number1*number2
    return result
print(multiply(3,4))


print (round(abs(float (input("Enter a number: ")))))
