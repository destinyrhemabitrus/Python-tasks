""" Exercise 2.14 """

age = int(input("How old are you: "))

maximumHeart_range = 220 - age
targetHeart_rangeOne = (maximumHeart_range * 50)/100
targetHeart_rangeTwo = (maximumHeart_range * 85)/100

print("Your maximum heart range is: ", maximumHeart_range, "and your target heart range is between: ",targetHeart_rangeOne, "to", targetHeart_rangeTwo)
