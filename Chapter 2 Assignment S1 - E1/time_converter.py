""" Time Converter """

time = int(input("Time in seconds: "))

hour = time//3600
hourRemainder = time%3600
minutes = hourRemainder//60
seconds = hourRemainder%60


print(hour, "Hours", minutes, "Minutes", seconds, "Seconds")


