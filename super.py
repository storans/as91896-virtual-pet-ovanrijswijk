# Check to see if someone is eligible for superannuation

# This age is a constant because it is not changed in the program
SUPER_AGE = 65

# Loop to allow testing of different values/ages
keep_going = ""
while keep_going == "":
    age = int(input("What is your age: "))

    # Must be greater than OR equal to catch 65 year olds
    if age >= SUPER_AGE:
        print("You can get super!!")
    else:
        print("Sorry you are too young to get a super")

    keep_going = input("If you want to keep going press enter else enter 'q': ")
