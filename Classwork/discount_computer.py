""" Algorithm """
#user enters an amount
#if amount is between 1000 to 10,000 get a 5% discount
# if amount is between 10,000 to 50,000 get a 10% discount
#if amount is 50,000 and above get a 20% discount


amount = float(input("Enter amount: "))

if(amount >= 1000 and amount<=10000):
    discount = (5/1000) * amount

elif(amount >= 10000 and amount<=50000):
    discount = (10/1000) * amount

else(amount > 50000):
    discount = (20/1000) * amount
    
print(dicount)

