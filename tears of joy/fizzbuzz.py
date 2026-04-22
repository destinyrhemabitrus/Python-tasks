for count in range(1, 51, 1):
    if count%3 == 0:
        print("fizz")
    elif count%5 == 0:
        print("buzz")
    elif count%5 == 0 and count%3 == 0:
        print("fizzbuzz")
    else:
        print(count)
    
