# Checks if the rabbit is out of weight range and if dead and then tells the user of rabbit is dead or not

# Asks the user to set the weight for testing purposes
weight = float(input("What weight do you want your rabbit to be: "))
# Set the name of the rabbit to Herb for testing purposes
name = "Herb"

if 1.5 <= weight <= 2.5:
    keep_going = ""
    print("Game continues")
else:
    print("Sorry, {} died".format(name))
    if 1.5 > weight:
         print("{} was underweight".format(name))
         print("{}'s weight was {}".format(name, weight))
    if 2.5 < weight:
         print("{} was overweight".format(name))
         print("{}'s weight was {}".format(name, weight))

    keep_going = "g" # Game ends
    print("Game ends")
