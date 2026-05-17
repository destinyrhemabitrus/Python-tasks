passes = 0
failures = 0
result = int(input('Enter result (1=pass, 2=fail): '))
while result != 1 and result !=2:
    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1
    result = int(input('Enter result (1=pass, 2=fail): '))

print(failures)


