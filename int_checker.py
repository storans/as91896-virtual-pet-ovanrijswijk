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

# Asks the user for the weight for testing purposes
activity = check_int("Please enter the number of the activity - make sure it is between 1 and 5", "Please enter a number between 1 and 5", 1, 5)
