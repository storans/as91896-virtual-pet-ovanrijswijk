# Functions
# Integer checker
def check_int(question, error, low, high): # I used question, error, low and high so I can use the check integer function for different things
    valid = False
    while valid == False:
        number = input("{}: ".format(question)) # The question is customised to the question
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error) # The error message is customised to the question


# Float checker
def check_float(question, error, low, high): # I used question, error, low and high so I can use the check float function for different things
    valid = False
    while valid == False:
        number = input("{}: ".format(question)) # The question is customised to the question
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error) # The error message is customised to the question


# Changes the weight of the rabbit based on the food or exercise the user picks
def weight_change(weight, picked, list):
    if picked == 1:
        weight += list[0][1]
    if picked == 2:
        weight += list[1][1]
    if picked == 3:
        weight += list[2][1]
    return weight


# Main routine
if __name__ == "__main__":
    FOOD_LIST = [["Kale", 0.1], ["Broccoli", 0.2], ["Apple", 0.4]]
    EXERCISE_LIST = [["Hopping", -0.3], ["Running", -0.5], ["Walking", -0.1]]

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
