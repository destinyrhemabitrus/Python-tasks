counter = 1
accumulator = 1;
number = int(input("Enter a number: "))
while(counter <= number):
    accumulator = accumulator * counter
    counter += 1
print(accumulator)
