"""A script that generates multiplication table """

for number in range(1,10,1):
    for count in range (number, 0, -1):
        print(count, end=" ")

    print()
