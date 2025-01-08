# test
# test
import random

number_of_simulations = 100000
change_answer = True
win = 0
lose = 0

for i in range(number_of_simulations):
    # prize
    prize = random.randint(0,2)
    # print("Prize: ", prize)

    # pick
    pick = random.randint(0,2)
    # print("Pick: ", pick)

    # remove
    remove = random.randint(0,2)
    while(remove == prize or remove == pick): remove = random.randint(0,2)
    # print("Remove" , remove)

    # change
    if change_answer:
        for j in range(3):
            if j != pick and j != remove:
                pick = j
                break

    if pick == prize:
        # print("win")
        win+=1
    else:
        # print("lose")
        lose+=1

print("Win: ", win)
print("Lose: ", lose)
print("Winning percentage: ", win/number_of_simulations*100)



