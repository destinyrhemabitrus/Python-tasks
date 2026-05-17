""" Letter Grade"""

score = float(input("Enter student score btw 0 to 100: "))

if (score >= 90):
    print("Grade: A")

elif (score >= 80):
        print("Grade: B")

elif (score >= 70):
        print("Grade: C")

elif (score >= 60):
        print("Grade: D")

elif (score >= 0):
        print("Grade: F")

else:
    print("Invalid input")


