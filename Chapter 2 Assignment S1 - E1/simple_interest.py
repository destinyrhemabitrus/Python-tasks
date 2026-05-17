""" Simple Interest"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time)/100

total_a = principal + si

print("Simple interest: ",si,"total amount: ",total_a)


