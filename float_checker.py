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


# Asks the user for the weight for testing purposes
weight = check_float("Please enter the weight you want your rabbit to be - make sure the weight is between 1.5 and 2.5", "Please enter the weight between 1.5 and 2.5", 1.5, 2.5)
