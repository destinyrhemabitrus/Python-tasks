"""A python program to create the multiplication table (from 1 to 10) of a given number """
#Set counter to 1
#Set total, count to 0
# while counter is less than 10
#   do result = 5 * counter, count = count + 1
#Increment counter by 1

counter = 1
total = 0
count = 0
while(counter <= 10):
    result = 5 * counter
    count = count + 1    
    counter += 1
    

    print(f"5 X {count} = {result}")
