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

#3.14 -