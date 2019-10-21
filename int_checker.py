# A function that will check if what the user inputs is an integer, if the user something
def check_int(question, error):
    valid = False

    while valid == False:
        number = input("{}: ".format(question))
        try:
          number = int(number)
          return number
        except ValueError:
            print(error)

sport = check_int("Please enter your chosen sport", "Please enter only the number of the sport")
