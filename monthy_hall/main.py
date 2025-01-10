import random

# Setup
DEFAULT = False

number_of_simulations = 10000
change_answer = True
total_boxes = 10
total_remove = 3

# Simulation

number_of_simulations = number_of_simulations if not DEFAULT else 10000
change_answer = change_answer if not DEFAULT else True
total_boxes = total_boxes if not DEFAULT else 3
total_remove = total_remove if not DEFAULT else 1

win = 0
lose = 0

for i in range(number_of_simulations):

    prize = random.randint(1,total_boxes)

    pick = random.randint(1,total_boxes)

    removed_list = []
    removed = total_remove

    while(removed != 0):
        remove = random.randint(1,total_boxes)
        if remove != prize and remove != pick and remove not in removed_list:
            removed_list.append(remove)
            removed -= 1

    if change_answer:
        previous_pick = pick
        while(True):
            pick = random.randint(1,total_boxes)
            if pick not in removed_list and pick != previous_pick:
                break

    if pick == prize:
        win += 1
    else:
        lose += 1

print("Removed list: ", removed_list)
print("Win: ", win)
print("Lose: ", lose)
print("Winning percentage: ", win/number_of_simulations*100)