import random

# Setup
number_of_simulations = 100000
change_answer = True
total_boxes = 100


win = 0
lose = 0

for i in range(number_of_simulations):

    prize = random.randint(1,total_boxes)
    # print("Prize: ", prize)

    pick = random.randint(1,total_boxes)
    # print("Pick: ", pick)

    # NO NEED REMOVE LOL
    remove = random.randint(1,total_boxes)
    while(remove == prize or remove == pick): remove = random.randint(1,total_boxes)
    # print("Remove" , remove)

    if change_answer:
        if pick == prize:
            lose += 1
        else:
            win += 1

    # if pick == prize:
    #     # print("win")
    #     win+=1
    # else:
    #     # print("lose")
    #     lose+=1

print("Win: ", win)
print("Lose: ", lose)
print("Winning percentage: ", win/number_of_simulations*100)



