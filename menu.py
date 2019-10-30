# Menu for the user to pick the options of what to do with there rabbit
EXERCISE_DICT = {"Hopping": -0.3, "Running": -0.5, "Walking": -0.1}
FOOD_DICT = {"Kale": 0.1, "Broccoli": 0.2, "Apple": 0.4}

name = input("What do you want to call your rabbit: ").strip().title()


print("Please choose what you want to do with {} from the following menu".format(name))
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
choice = int(input("Enter the number of what you want to do with {}: ".format(name)))

# If the user chooses option 1

if choice == 1:
    print("Feed {}".format(name))
    number = 1
    for food in FOOD_DICT:
        print("{}. {}".format(number, food.title()))
        number += 1
    option = int(input("Enter the number of what you want to feed {}: ".format(name)))

    if option == 1:
        print("Kale")
    if option == 2:
        print("Broccoli")
    if option == 3:
        print("Apple")
# If the user chooses option 2
if choice == 2:
    print("Exercise {}".format(name))
    number = 1
    for exercise in EXERCISE_DICT:
        print("{}. {}".format(number, exercise.title()))
        number += 1
    option = int(input("Enter the number of what exercise you want {} do: ".format(name)))
# If the user chooses option 3
if choice == 3:
    print("Check {}'s weight".format(name))
    # weight will go here
# If the user chooses option 4
if choice == 4:
    print("See help information")
    print("To keep {} alive, make sure you feed it the right food and the right amount of exercise.".format(name))
    print("Eating food will make {}'s weight go up and exercise will bring {}'s weight down.".format(name, name))
    print("If {}'s weight goes outside of the weight range of 1.5kg to 2.5kg {} will die.".format(name, name))
if choice == 5:
    print("End game")
    # Set keep_going to 'q'
