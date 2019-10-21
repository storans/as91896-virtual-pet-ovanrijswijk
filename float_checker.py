def check_float(question, error, low, high): # Question and error allow it to be used in a range of situations
    valid = False

    while valid == False:
        number = input("{}: ".format(question)) # Any question that needs a number
        try:
            number = float(number)
            if low <= number <= high:
                return number # Note, I do not set valid to True, as returning does this
            else:
                print(error)
        except ValueError:
            print(error) # Customised to the question!

weight = check_float("Please enter the weight you want your rabbit to be - make sure the weight is between 1.5 and 2.5", "Please enter the weight between 1.5 and 2.5", 1.5, 2.5)
