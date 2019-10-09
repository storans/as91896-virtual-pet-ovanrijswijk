SUPER_AGE = 65
keep_going = ""
while keep_going == "":
    age = int(input("What is your age: "))
    if age >= SUPER_AGE:
        print("You can get super!!")
        keep_going = input("If you want to keep going press enter: ")
    else:
        print("Sorry you are too young to get a super")
        keep_going = input("If you want to keep going press enter: ")
