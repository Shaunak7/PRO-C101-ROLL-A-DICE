import random
roll_again = "y"
while roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    value1=random.randint(1,6)
    value2=random.randint(1,6)
    print(value1,value2)
    roll_again = input("Press 'y' to roll the dices again or 'n' to stop.")

if roll_again == "n":
    print("Have a good day!!")