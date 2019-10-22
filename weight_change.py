def weight_change(weight, picked, list):

    if picked == 1:
        weight += list[0][1]

    if picked == 2:
        weight += list[1][1]

    if picked == 3:
        weight += list[2][1]

    return weight

weight = float(input("Please set the weight of {}. The weight should be between 1.5 - 2.5: "))
EXERCISE_LIST = [["Hopping", -0.3], ["Running", -0.5], ["Walking", -0.1]]
FOOD_LIST = [["Kale", 0.1], ["Broccoli", 0.2], ["Apple", 0.4]]

picked = int(input("What do you want to eat: "))

changed_weight = weight_change(weight, picked, FOOD_LIST)
print(changed_weight)
