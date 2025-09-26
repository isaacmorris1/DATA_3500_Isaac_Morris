#3.4 -
for row in range(2):
    for column in range(7):
        print("@", end=" ")
    print()

#3.9 -
UserNum = int(input("Please enter a number that has between 7 to 10 digits: "))
while UserNum > 0:
    length = len(str(UserNum))
    FloorD = 10 ** (length-1)
    digit = UserNum // FloorD
    UserNum -= (FloorD * digit)
    print(digit)

#3.11 -
counter = 0
total = 0
while True:
    gallons = float(input("Enter the gallons used or type -1 to end: "))
    if gallons == -1:
        break
    miles = float(input("Enter the number of miles driven: "))
    mpg = miles / gallons
    print("The miles per gallon for this tank was", str(mpg) + ".")
    counter += 1
    total += mpg
if counter > 0:
    finalmpg = total / counter
    print("The overall miles per gallon was", str(finalmpg) + ".")

#3.12 -
palindrome = int(input("Enter a five digit number: "))
First = palindrome // 10000
Second = (palindrome // 1000) % 10
Fourth = (palindrome // 10) % 10
Fifth = palindrome % 10
print(First, Second, Fourth, Fifth)
if First == Fifth and Second == Fourth:
    print("Palindrome!!!!")
else:
    print("Not a palindrome....")

#3.14 - (THIS MADE MY BRAIN HURT. I think I made it way more complicated than it needed to be.)
denominator = 3
pi = 4
signflip = -1
firstcheck = False
secondcheck = False
f3 = 0
f2 = 0
for i in range(1, 3001):
    previouspi = pi
    previousf2 = f2
    previousf3 = f3
    pi += (signflip * (4 / denominator))
    denominator += 2
    signflip *= -1
    if firstcheck == False:
        f2 = f"{pi:.2f}"
        if previousf2 == f2:
            firstcheck = True
            print("It first hits 3.14 twice in a row at iteration", i)
    elif secondcheck == False:
        f3 = f"{pi:.3f}"
        if previousf3 == f3:
            secondcheck = True
            print("It first hits 3.141 twice in a row at iteration", i)