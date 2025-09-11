#2.3
grade = int(input("What is your grade percentage?: "))
if grade >= 90:
    print("Congratulations! Your grade of " + str(grade) + " earns you an A in this course!")
else:
    print("Not quite an A, but keep up the hard work!")

#2.4
left = 27.5
right = 2
add = left + right
minus = left - right
multiply = left * right
divide = left / right
modulo = left // right
exponent = left ** right
print(add, minus, multiply, divide, modulo, exponent)

#2.5
pi = 3.14159
radius = 2
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * (radius ** 2)
print(diameter, circumference, area)

#2.6
UserNum = int(input("Enter a whole number: "))
if UserNum % 2 == 0:
    print(str(UserNum) + " is even.")
else:
    print(str(UserNum) + " is odd.")

#2.7
if 1024 % 4 == 0:
    print("1024 is a multiple of 4.")
else:
    print("1024 is not a multiple of 4.")
if 2 % 10 == 0:
    print("2 is a multiple of 10.")
else:
    print("2 is not a multiple of 10.")

#2.8
print("number\t square\t cube")
for num in range(6):
    print(f"{num}\t {num**2}\t {num**3}")