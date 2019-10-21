# How the program will start
print("Welcome to Virtual Rabbit")
print("")
# The users rabbit
print("(\_/) \n"
      "(o.o) \n"
      "(___)O \n")
name = input("What do you want to name your rabbit: ")
print("")
# Help information so the user knows how to play the game
print("To keep {} alive, make sure you feed it the right food and the right amount of exercise.".format(name))
print("Eating food will make {}'s weight go up and exercise will bring {}'s weight down.".format(name, name))
print("If {}'s weight goes outside of the weight range of 1.5kg to 2.5kg {} will die.".format(name, name))
