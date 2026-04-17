#Colect password from user
#if password is less than 8 print very weak
#if password is 8 print weak 
#if password is between 8 and 16 print strong
#if password is above 16 print very strong

password = input("Enter your password")
 
if(len(password)>= 9 and len(password) <=16):
    print("Strong")

elif(len(password) < 8):
    print("very Weak")

elif(len(password) == 8):
    print("Weak")

elif(len(password) > 16):
    print("Very strong")





