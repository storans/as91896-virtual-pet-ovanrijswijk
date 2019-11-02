# Functions


# Integer checker
def check_int(question, error, low, high):  # I used question, error, low and
    # high so I can use the check integer function for different things
    valid = False
    while not valid:
        number = input("{}: ".format(question))  # The question is customised
        # to the question
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)  # The error message is customised


# Float checker
def check_float(question, error, low, high):  # I used question, error, low
    # and high so I can use the check float function for different things
    valid = False
    while not valid:
        number = input("{}: ".format(question))  # The question is customised
        # to the question
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)  # The error message is customised


# Changes the weight of the rabbit based on the food or exercise the user picks
def weight_change(weight, option, list):
    option - 1  # so the option the user chooses matches up with the value in
    # the list
    # If the user chooses option 1
    if option == 1:
        weight += list[0][1]  # Adds the weight value from the list to the
        # current weight of the rabbit
    # if the user chooses option 2
    if option == 2:
        weight += list[1][1]  # Adds the weight value from the list to the
        # current weight of the rabbit
    # If the user chooses option 3
    if option == 3:
        weight += list[2][1]  # Adds the weight value from the list to the
        # current weight of the rabbit

    return weight


# Check if the rabbit is dead or not based off its weight - if over or
# underweight the rabbit dies and the game ends
def death_check(weight, name):
    # If the weight of the rabbit is between 1.5 and 2.5 the game keeps going
    if 1.5 <= weight <= 2.5:
        keep_going = ""
    # If the weight of the rabbit is outside the weight range of 1.5 - 2.5 the
    # rabbit dies and the game ends
    else:
        print("Sadly, {} died.".format(name))
        # If the rabbits weight was under 1.5 tells the user what to do next
        # time
        if 1.5 > weight:
            print("{} was underweight. Maybe next time feed your animal "
                  "slightly more.".format(name))
            print("{}'s weight when they died was {}".format(name, weight))
        # If the rabbits weight was over 2.5 tells the user what to do next
        # time
        if 2.5 < weight:
            print("{} was overweight. Maybe next time exercise your animal "
                  "slightly more.".format(name))
            print("{}'s weight when they died was {}".format(name, weight))
        keep_going = "g"  # Game ends
    return keep_going


# Main routine
if __name__ == "__main__":

    # Food and exercise list and dictionaries
    FOOD_LIST = [["Kale", 0.1], ["Broccoli", 0.2], ["Apple", 0.4]]
    FOOD_DICT = {"Kale": 0.1, "Broccoli": 0.2, "Apple": 0.4}
    EXERCISE_DICT = {"Hopping": -0.3, "Running": -0.5, "Walking": -0.1}
    EXERCISE_LIST = [["Hopping", -0.3], ["Running", -0.5], ["Walking", -0.1]]


    print("Welcome to Virtual Rabbit")
    print("")
    # The users rabbit
    print("(\_/) \n"
          "(o.o) \n"
          "(___)O \n")
    name = input("What do you want to name your rabbit: ").strip().title()
    print("")
    # Help information so the user knows how to play the game
    print("To keep {} alive, make sure you feed it the right food and the "
          "right amount of exercise.".format(name))
    print("Eating food will make {}'s weight go up and exercise will bring "
          "{}'s weight down.".format(name, name))
    print("If {}'s weight goes outside of the weight range of 1.5kg to 2.5kg "
          "{} will die.".format(name, name))
    print("")
    # User sets the weight of the rabbit
    weight = check_float("What do you want {}'s weight to be - remember to "
                         "have it between 1.5 and 2.5".format(name), "Please "
                         "enter a weight between 1.5 and 2.5", 1.5, 2.5)

    # Main Menu and sub menus
    keep_going = ""
    while keep_going == "":
        print("")
        print("Please choose what you want to do with {} from the following "
              "menu".format(name))
        # Main menu
        print("1. Feed {}"
              " "
              " "
              " "
              "2. Exercise {}"
              " "
              " "
              " "
              "3. Check {}'s weight"
              " "
              " "
              " "
              "4. See help information"
              " "
              " "
              " "
              "5. End game".format(name, name, name))
        print("")
        # Make this a check-int in the version
        choice = check_int("Enter the number of what you want to do with {}:"
                           " ".format(name), "Please enter a number between 1 "
                                             "and 5", 1, 5)
        # Sub menu
        # If the user chooses to feed their rabbit
        if choice == 1:
            print("Feed {}".format(name))
            number = 1
            for food in FOOD_DICT:
                print("{}. {}".format(number, food.title()))
                number += 1
            option = check_int("Enter the number of what you want to feed"
                               " {}: ".format(name), "Please enter a number "
                                                     "between 1 and 3", 1, 3)
            # If the user chooses kale
            if option == 1:
                print("{} is going to eat a kale leaf".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, FOOD_LIST)
            # If the user chooses broccoli
            if option == 2:
                print("{} is going to eat a bowl of broccoli".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, FOOD_LIST)
            # If the user chooses apple
            if option == 3:
                print("{} is going to eat a whole apple".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, FOOD_LIST)
            # print the current weight so the user knows
            print("{} currently weighs {} kg".format(name, weight))
            # Check if the rabbit should be dead based off weight and if the
            # game should end
            keep_going = death_check(weight, name)
        # If the user chooses to exercise their rabbit
        elif choice == 2:
            print("Exercise {}".format(name))
            number = 1
            for exercise in EXERCISE_DICT:
                print("{}. {}".format(number, exercise.title()))
                number += 1
            option = check_int("Enter the number of what exercise you want {} "
                               "do: ".format(name), "Please enter a number "
                                                    "between 1 and 3", 1, 3)
            print("")
            #  If the user chooses hopping
            if option == 1:
                print("{} is going to do some hopping".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, EXERCISE_LIST)
            # If the user chooses running
            if option == 2:
                print("{} is going to go for a run".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, EXERCISE_LIST)
            # If the user chooses walking
            if option == 3:
                print("{} is going to go walking".format(name))
                # changes the weight of the rabbit based off the value of the
                # food chosen
                weight = weight_change(weight, option, EXERCISE_LIST)
            # print the weight of the rabbit so the user knows
            print("{} currently weighs {} kg".format(name, weight))
            # Check if the rabbit should be dead based off weight and if the
            # game should end
            death_check(weight, name)
        # If the user chooses to see the weight of their rabbit
        elif choice == 3:
            print("Check {}'s Weight".format(name))
            print("{}'s weight currently is: ")
            print("{} kgs".format(weight))
        # If the user chooses to see the help information
        elif choice == 4:
            print("See help information")
            print("To keep {} alive, make sure you feed it the right food and"
                  " the right amount of exercise.".format(name))
            print("Eating food will make {}'s weight go up and exercise will "
                  "bring {}'s weight down.".format(name, name))
            print("If {}'s weight goes outside of the weight range of 1.5kg to"
                  " 2.5kg {} will die.".format(name, name))
        # If the user wants to end the game
        else:
            # Asks the user if they are sure they want to end the game
            keep_going = input("If you don't want to end the game press enter"
                               " - If you are sure you want to end the game "
                               "enter 'q': ")
            # If the user inputs anything that isn't the enter button the game
            # ends and their rabbit says goodbye
            if keep_going != "":
                print("{} says goodbye!!".format(name))
