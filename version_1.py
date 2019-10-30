# Functions


# Integer checker
def check_int(question, error, low, high):  # I used question, error, low and
    # high so I can use the check integer function for different things
    valid = False
    while valid == False:
        number = input("{}: ".format(question))  # The question is customised
        # to the question
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)  # The error message is customised to the question


# Float checker
def check_float(question, error, low, high):  # I used question, error, low
    # and high so I can use the check float function for different things
    valid = False
    while valid == False:
        number = input("{}: ".format(question))  # The question is customised
        # to the question
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)  # The error message is customised to the question


# Changes the weight of the rabbit based on the food or exercise the user picks
def weight_change(weight, option, list):
    option - 1
    if option == 1:
        weight += list[0][1]

    if option == 2:
        weight += list[1][1]

    if option == 3:
        weight += list[2][1]

    return weight


# Check if the rabbit is dead or not based off its weight - if over or
# underweight the rabbit dies and the game ends
def death_check(weight, name):
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
    return keep_going


# Main routine
if __name__ == "__main__":

    FOOD_LIST = [["Kale", 0.1], ["Broccoli", 0.2], ["Apple", 0.4]]
    EXERCISE_LIST = [["Hopping", -0.3], ["Running", -0.5], ["Walking", -0.1]]
    EXERCISE_DICT = {"Hopping": -0.3, "Running": -0.5, "Walking": -0.1}
    FOOD_DICT = {"Kale": 0.1, "Broccoli": 0.2, "Apple": 0.4}

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
    weight = check_float("What do you want {}'s weight to be - remember to "
                         "have it between 1.5 and 2.5".format(name), "Please "
                         "enter a weight between 1.5 and 2.5", 1.5, 2.5)

    # Main Menu and sub menus
    keep_going = ""
    while keep_going == "":
        print("Please choose what you want to do with {} from the following "
              "menu".format(name))
        print("1. Feed {}"
              " "
              " "
              "2. Exercise {}"
              " "
              " "
              "3. Check {}'s weight"
              " "
              " "
              "4. See help information"
              " "
              " "
              "5. End game".format(name, name, name))
        # Make this a check-int in the version
        choice = check_int("Enter the number of what you want to do with {}:"
                           " ".format(name), "Please enter a number between 1 "
                                             "and 5", 1, 5)

        # If the user chooses option 1

        if choice == 1:
            print("Feed {}".format(name))
            number = 1
            for food in FOOD_DICT:
                print("{}. {}".format(number, food.title()))
                number += 1
            option = check_int("Enter the number of what you want to feed"
                               " {}: ".format(name), "Please enter a number "
                                                     "between 1 and 3", 1, 3)

            if option == 1:
                print("Kale")
                weight = weight_change(weight, option, FOOD_LIST)
            if option == 2:
                print("Broccoli")
                weight = weight_change(weight, option, FOOD_LIST)
            if option == 3:
                print("Apple")
                weight = weight_change(weight, option, FOOD_LIST)
            print("{} currently weighs {} kg".format(name, weight))
            keep_going = death_check(weight, name)
        # If the user chooses option 2
        if choice == 2:
            print("Exercise {}".format(name))
            number = 1
            for exercise in EXERCISE_DICT:
                print("{}. {}".format(number, exercise.title()))
                number += 1
            option = check_int("Enter the number of what exercise you want {} "
                               "do: ".format(name), "Please enter a number "
                                                    "between 1 and 3", 1, 3)

            if option == 1:
                print("Hopping")
                weight = weight_change(weight, option, EXERCISE_LIST)
                print("{} currently weighs {} kg".format(name, weight))
            if option == 2:
                print("Running")
                weight = weight_change(weight, option, EXERCISE_LIST)
                print("{} currently weighs {} kg".format(name, weight))
            if option == 3:
                print("Walking")
                weight = weight_change(weight, option, EXERCISE_LIST)
                print("{} currently weighs {} kg".format(name, weight))
            death_check(weight, name)
        # If the user chooses option 3
        if choice == 3:
            print("Check {}'s weight".format(name))
            print(weight)
            death_check(weight, name)
        # If the user chooses option 4
        if choice == 4:
            print("See help information")
            print("To keep {} alive, make sure you feed it the right food and"
                  " the right amount of exercise.".format(name))
            print("Eating food will make {}'s weight go up and exercise will "
                  "bring {}'s weight down.".format(name, name))
            print("If {}'s weight goes outside of the weight range of 1.5kg to"
                  " 2.5kg {} will die.".format(name, name
        if choice == 5:
            print("End game")

