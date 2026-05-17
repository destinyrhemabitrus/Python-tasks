""" Exercise 2.10 """

numberOne = int(input('Enter first number: '))
numberTwo = int(input('Enter Second number: '))
numberThree = int(input('Enter Third number: '))

summ= numberOne + numberTwo + numberThree
product = numberOne * numberTwo * numberThree
average = (numberOne + numberTwo + numberThree)/3

largest = numberOne

if(numberTwo > largest):
    largest = numberTwo

if(numberThree > largest):
    largest = numberThree

smallest = numberOne

if(numberTwo < smallest):
    smallest = numberTwo

if(numberThree < smallest):
    smallest = numberThree

print("Sum: ",summ)
print("Average: ",average)
print("Product: ",product)
print("Smallest of the numbers is : ",smallest)
print("Largest of the numbers is: ",largest)



