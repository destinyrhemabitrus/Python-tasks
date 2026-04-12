""" MortgageCalculator"""

amount = float(input("Enter amount you want to borrow: "))
rate = float(input("Enter Annual interest Rate for this amount: "))
duration = float(input("How long is this mortgage for: "))

percentage_rate =  ((rate)/100)/(12)
total_duration = duration * 12;
monthly_rate = amount * ((percentage_rate * ((1 + percentage_rate) ** total_duration))/(((1 + percentage_rate) ** total_duration) - 1))

print("Your monthly payment is: ",monthly_rate)


