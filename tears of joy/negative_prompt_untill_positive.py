number = int(input("Enter a number: "))
while(number <= 0):
    number = int(input("Enter a number: "))
    if number > 0:
        break
print(f"You entered: {number}")

